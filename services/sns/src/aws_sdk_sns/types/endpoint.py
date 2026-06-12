"""Generated from Smithy shape ``com.amazonaws.sns#Endpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.map_string_to_string
    import aws_sdk_sns.types.string


class Endpoint(TypedDict):
    endpoint_arn: NotRequired["aws_sdk_sns.types.string.String"]
    """<p>The <code>EndpointArn</code> for mobile app and device.</p>"""
    attributes: NotRequired["aws_sdk_sns.types.map_string_to_string.MapStringToString"]
    """<p>Attributes for endpoint.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Endpoint, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "endpoint_arn" in value:
        pairs.append((f"{prefix}.EndpointArn", str(value["endpoint_arn"])))
    if "attributes" in value:
        import aws_sdk_sns.types.map_string_to_string

        aws_sdk_sns.types.map_string_to_string.serialize_query(
            value["attributes"], pairs, f"{prefix}.Attributes"
        )


def deserialize_query(el: Element) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    child_endpoint_arn = el.find("EndpointArn")
    if child_endpoint_arn is not None:
        out["endpoint_arn"] = str(child_endpoint_arn.text or "")
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import aws_sdk_sns.types.map_string_to_string

        out["attributes"] = aws_sdk_sns.types.map_string_to_string.deserialize_query(
            child_attributes
        )
    return out
