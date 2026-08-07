"""Generated from Smithy shape ``com.amazonaws.sns#GetSMSAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.map_string_to_string


class GetSMSAttributesResponse(TypedDict, closed=True):
    attributes: NotRequired["capo_sns.types.map_string_to_string.MapStringToString"]
    """<p>The SMS attribute names and their values.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSMSAttributesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attributes" in value:
        import capo_sns.types.map_string_to_string

        capo_sns.types.map_string_to_string.serialize_query(
            value["attributes"], pairs, f"{key_prefix}attributes"
        )


def deserialize_query(el: Element) -> GetSMSAttributesResponse:
    out: GetSMSAttributesResponse = {}  # type: ignore[typeddict-item]
    child_attributes = el.find("attributes")
    if child_attributes is not None:
        import capo_sns.types.map_string_to_string

        out["attributes"] = capo_sns.types.map_string_to_string.deserialize_query(
            child_attributes
        )
    return out
