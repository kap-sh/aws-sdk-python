"""Generated from Smithy shape ``com.amazonaws.rds#MinimumEngineVersionPerAllowedValueList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.minimum_engine_version_per_allowed_value

MinimumEngineVersionPerAllowedValueList: TypeAlias = list[
    "capo_rds.types.minimum_engine_version_per_allowed_value.MinimumEngineVersionPerAllowedValue"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: MinimumEngineVersionPerAllowedValueList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_rds.types.minimum_engine_version_per_allowed_value

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.minimum_engine_version_per_allowed_value.serialize_query(
            item, pairs, f"{prefix}.MinimumEngineVersionPerAllowedValue.{n}"
        )


def deserialize_query(el: Element) -> MinimumEngineVersionPerAllowedValueList:
    import capo_rds.types.minimum_engine_version_per_allowed_value

    out: MinimumEngineVersionPerAllowedValueList = []
    for child in el.findall("MinimumEngineVersionPerAllowedValue"):
        out.append(
            capo_rds.types.minimum_engine_version_per_allowed_value.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: MinimumEngineVersionPerAllowedValueList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_rds.types.minimum_engine_version_per_allowed_value

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.minimum_engine_version_per_allowed_value.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> MinimumEngineVersionPerAllowedValueList:
    import capo_rds.types.minimum_engine_version_per_allowed_value

    out: MinimumEngineVersionPerAllowedValueList = []
    for child in parent.findall(tag):
        out.append(
            capo_rds.types.minimum_engine_version_per_allowed_value.deserialize_query(
                child
            )
        )
    return out
