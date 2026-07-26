"""Generated from Smithy shape ``com.amazonaws.elasticache#DataStorage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.data_storage_unit
    import capo_elasticache.types.integer_optional


class DataStorage(TypedDict, closed=True):
    maximum: NotRequired["capo_elasticache.types.integer_optional.IntegerOptional"]
    """<p>The upper limit for data storage the cache is set to use.</p>"""
    minimum: NotRequired["capo_elasticache.types.integer_optional.IntegerOptional"]
    """<p>The lower limit for data storage the cache is set to use.</p>"""
    unit: NotRequired["capo_elasticache.types.data_storage_unit.DataStorageUnit"]
    """<p>The unit that the storage is measured in, in GB.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DataStorage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "maximum" in value:
        pairs.append((f"{prefix}.Maximum", str(value["maximum"])))
    if "minimum" in value:
        pairs.append((f"{prefix}.Minimum", str(value["minimum"])))
    if "unit" in value:
        import capo_elasticache.types.data_storage_unit

        capo_elasticache.types.data_storage_unit.serialize_query(
            value["unit"], pairs, f"{prefix}.Unit"
        )


def deserialize_query(el: Element) -> DataStorage:
    out: DataStorage = {}  # type: ignore[typeddict-item]
    child_maximum = el.find("Maximum")
    if child_maximum is not None:
        out["maximum"] = int(child_maximum.text or "")
    child_minimum = el.find("Minimum")
    if child_minimum is not None:
        out["minimum"] = int(child_minimum.text or "")
    child_unit = el.find("Unit")
    if child_unit is not None:
        import capo_elasticache.types.data_storage_unit

        out["unit"] = capo_elasticache.types.data_storage_unit.deserialize_query(
            child_unit
        )
    return out
