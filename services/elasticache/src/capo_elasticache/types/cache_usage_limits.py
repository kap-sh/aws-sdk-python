"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheUsageLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.data_storage
    import capo_elasticache.types.ecpu_per_second


class CacheUsageLimits(TypedDict, closed=True):
    data_storage: NotRequired["capo_elasticache.types.data_storage.DataStorage"]
    """<p> The maximum data storage limit in the cache, expressed in Gigabytes. </p>"""
    ecpu_per_second: NotRequired["capo_elasticache.types.ecpu_per_second.ECPUPerSecond"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheUsageLimits, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "data_storage" in value:
        import capo_elasticache.types.data_storage

        capo_elasticache.types.data_storage.serialize_query(
            value["data_storage"], pairs, f"{key_prefix}DataStorage"
        )
    if "ecpu_per_second" in value:
        import capo_elasticache.types.ecpu_per_second

        capo_elasticache.types.ecpu_per_second.serialize_query(
            value["ecpu_per_second"], pairs, f"{key_prefix}ECPUPerSecond"
        )


def deserialize_query(el: Element) -> CacheUsageLimits:
    out: CacheUsageLimits = {}  # type: ignore[typeddict-item]
    child_data_storage = el.find("DataStorage")
    if child_data_storage is not None:
        import capo_elasticache.types.data_storage

        out["data_storage"] = capo_elasticache.types.data_storage.deserialize_query(
            child_data_storage
        )
    child_ecpu_per_second = el.find("ECPUPerSecond")
    if child_ecpu_per_second is not None:
        import capo_elasticache.types.ecpu_per_second

        out["ecpu_per_second"] = (
            capo_elasticache.types.ecpu_per_second.deserialize_query(
                child_ecpu_per_second
            )
        )
    return out
