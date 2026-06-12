"""Generated from Smithy shape ``com.amazonaws.ram#UpdateResourceShareResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.resource_share
    import aws_sdk_ram.types.string


class UpdateResourceShareResponse(TypedDict):
    resource_share: NotRequired["aws_sdk_ram.types.resource_share.ResourceShare"]
    """<p>Information about the resource share.</p>"""
    client_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the <code>clientToken</code> request parameter of that later call. All other parameters must also have the same values that you used in the first call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceShareResponse) -> dict:
    out: dict = {}
    if "resource_share" in value:
        import aws_sdk_ram.types.resource_share

        out["resourceShare"] = aws_sdk_ram.types.resource_share.serialize_json(
            value["resource_share"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateResourceShareResponse:
    out: UpdateResourceShareResponse = {}  # type: ignore[typeddict-item]
    if "resourceShare" in data:
        import aws_sdk_ram.types.resource_share

        out["resource_share"] = aws_sdk_ram.types.resource_share.deserialize_json(
            data["resourceShare"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
