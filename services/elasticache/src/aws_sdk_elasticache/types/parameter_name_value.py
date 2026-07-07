"""Generated from Smithy shape ``com.amazonaws.elasticache#ParameterNameValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class ParameterNameValue(TypedDict, closed=True):
    parameter_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the parameter.</p>"""
    parameter_value: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The value of the parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ParameterNameValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "parameter_name" in value:
        pairs.append((f"{prefix}.ParameterName", str(value["parameter_name"])))
    if "parameter_value" in value:
        pairs.append((f"{prefix}.ParameterValue", str(value["parameter_value"])))


def deserialize_query(el: Element) -> ParameterNameValue:
    out: ParameterNameValue = {}  # type: ignore[typeddict-item]
    child_parameter_name = el.find("ParameterName")
    if child_parameter_name is not None:
        out["parameter_name"] = str(child_parameter_name.text or "")
    child_parameter_value = el.find("ParameterValue")
    if child_parameter_value is not None:
        out["parameter_value"] = str(child_parameter_value.text or "")
    return out
