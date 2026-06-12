"""Generated from Smithy shape ``com.amazonaws.apigateway#SdkTypes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_sdk_type


class SdkTypes(TypedDict):
    items: NotRequired["aws_sdk_api_gateway.types.list_of_sdk_type.ListOfSdkType"]
    """<p>The current page of elements from this collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SdkTypes) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_api_gateway.types.list_of_sdk_type

        out["item"] = aws_sdk_api_gateway.types.list_of_sdk_type.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> SdkTypes:
    out: SdkTypes = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import aws_sdk_api_gateway.types.list_of_sdk_type

        out["items"] = aws_sdk_api_gateway.types.list_of_sdk_type.deserialize_json(
            data["item"]
        )
    return out
