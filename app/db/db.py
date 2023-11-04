import aioredis


class RedisDB:
    address = aioredis.from_url("redis://localhost:6379/2")

    def __init__(self) -> None:
        self.redis = self.address

    async def set_data(self, key: str, value: str, ex):
        await self.redis.set(key, value, ex=ex)
        return "data is store"

    async def get_data(self, key: str):
        result = await self.redis.get(key)
        return result

    async def delete_data(self, key: str):
        await self.redis.delete(key)
        return f"{key} was deleted"
