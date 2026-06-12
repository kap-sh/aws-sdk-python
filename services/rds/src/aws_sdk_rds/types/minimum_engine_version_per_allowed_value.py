"""Generated from Smithy shape ``com.amazonaws.rds#MinimumEngineVersionPerAllowedValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class MinimumEngineVersionPerAllowedValue(TypedDict):
    allowed_value: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The allowed value for an option setting.</p>"""
    minimum_engine_version: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The minimum DB engine version required for the allowed value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MinimumEngineVersionPerAllowedValue,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "allowed_value" in value:
        pairs.append((f"{prefix}.AllowedValue", str(value["allowed_value"])))
    if "minimum_engine_version" in value:
        pairs.append(
            (f"{prefix}.MinimumEngineVersion", str(value["minimum_engine_version"]))
        )


def deserialize_query(el: Element) -> MinimumEngineVersionPerAllowedValue:
    out: MinimumEngineVersionPerAllowedValue = {}  # type: ignore[typeddict-item]
    child_allowed_value = el.find("AllowedValue")
    if child_allowed_value is not None:
        out["allowed_value"] = str(child_allowed_value.text or "")
    child_minimum_engine_version = el.find("MinimumEngineVersion")
    if child_minimum_engine_version is not None:
        out["minimum_engine_version"] = str(child_minimum_engine_version.text or "")
    return out
