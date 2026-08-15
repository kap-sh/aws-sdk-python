"""Generated from Smithy shape ``com.amazonaws.iam#GetAccountPropertiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.account_properties_map_type


class GetAccountPropertiesResponse(TypedDict, closed=True):
    properties: NotRequired[
        "capo_iam.types.account_properties_map_type.accountPropertiesMapType"
    ]
    """<p>A map of account property key-value pairs. Keys are in the format <code>Namespace/PropertyName</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetAccountPropertiesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "properties" in value:
        import capo_iam.types.account_properties_map_type

        capo_iam.types.account_properties_map_type.serialize_query(
            value["properties"], pairs, f"{key_prefix}Properties"
        )


def deserialize_query(el: Element) -> GetAccountPropertiesResponse:
    out: GetAccountPropertiesResponse = {}  # type: ignore[typeddict-item]
    child_properties = el.find("Properties")
    if child_properties is not None:
        import capo_iam.types.account_properties_map_type

        out["properties"] = (
            capo_iam.types.account_properties_map_type.deserialize_query(
                child_properties
            )
        )
    return out
