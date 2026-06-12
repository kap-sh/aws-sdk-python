"""Generated from Smithy shape ``com.amazonaws.sns#GetSMSAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.map_string_to_string


class GetSMSAttributesResponse(TypedDict):
    attributes: NotRequired["aws_sdk_sns.types.map_string_to_string.MapStringToString"]
    """<p>The SMS attribute names and their values.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSMSAttributesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attributes" in value:
        import aws_sdk_sns.types.map_string_to_string

        aws_sdk_sns.types.map_string_to_string.serialize_query(
            value["attributes"], pairs, f"{prefix}.attributes"
        )


def deserialize_query(el: Element) -> GetSMSAttributesResponse:
    out: GetSMSAttributesResponse = {}  # type: ignore[typeddict-item]
    child_attributes = el.find("attributes")
    if child_attributes is not None:
        import aws_sdk_sns.types.map_string_to_string

        out["attributes"] = aws_sdk_sns.types.map_string_to_string.deserialize_query(
            child_attributes
        )
    return out
