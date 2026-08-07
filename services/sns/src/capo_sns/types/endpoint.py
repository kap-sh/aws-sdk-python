"""Generated from Smithy shape ``com.amazonaws.sns#Endpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.map_string_to_string
    import capo_sns.types.string


class Endpoint(TypedDict, closed=True):
    endpoint_arn: NotRequired["capo_sns.types.string.String"]
    """<p>The <code>EndpointArn</code> for mobile app and device.</p>"""
    attributes: NotRequired["capo_sns.types.map_string_to_string.MapStringToString"]
    """<p>Attributes for endpoint.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Endpoint, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "endpoint_arn" in value:
        pairs.append((f"{key_prefix}EndpointArn", str(value["endpoint_arn"])))
    if "attributes" in value:
        import capo_sns.types.map_string_to_string

        capo_sns.types.map_string_to_string.serialize_query(
            value["attributes"], pairs, f"{key_prefix}Attributes"
        )


def deserialize_query(el: Element) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    child_endpoint_arn = el.find("EndpointArn")
    if child_endpoint_arn is not None:
        out["endpoint_arn"] = str(child_endpoint_arn.text or "")
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import capo_sns.types.map_string_to_string

        out["attributes"] = capo_sns.types.map_string_to_string.deserialize_query(
            child_attributes
        )
    return out
