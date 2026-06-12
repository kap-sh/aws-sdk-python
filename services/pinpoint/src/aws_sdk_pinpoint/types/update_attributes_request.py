"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.list_of__string


class UpdateAttributesRequest(TypedDict):
    blacklist: NotRequired["aws_sdk_pinpoint.types.list_of__string.ListOf__string"]
    """<p>An array of the attributes to remove from all the endpoints that are associated with the application. The array can specify the complete, exact name of each attribute to remove or it can specify a glob pattern that an attribute name must match in order for the attribute to be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAttributesRequest) -> dict:
    out: dict = {}
    if "blacklist" in value:
        import aws_sdk_pinpoint.types.list_of__string

        out["Blacklist"] = aws_sdk_pinpoint.types.list_of__string.serialize_json(
            value["blacklist"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAttributesRequest:
    out: UpdateAttributesRequest = {}  # type: ignore[typeddict-item]
    if "Blacklist" in data:
        import aws_sdk_pinpoint.types.list_of__string

        out["blacklist"] = aws_sdk_pinpoint.types.list_of__string.deserialize_json(
            data["Blacklist"]
        )
    return out
