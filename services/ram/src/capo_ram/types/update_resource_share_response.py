"""Generated from Smithy shape ``com.amazonaws.ram#UpdateResourceShareResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.resource_share
    import capo_ram.types.string


class UpdateResourceShareResponse(TypedDict, closed=True):
    resource_share: NotRequired["capo_ram.types.resource_share.ResourceShare"]
    """<p>Information about the resource share.</p>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the <code>clientToken</code> request parameter of that later call. All other parameters must also have the same values that you used in the first call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceShareResponse) -> dict:
    out: dict = {}
    if "resource_share" in value:
        import capo_ram.types.resource_share

        out["resourceShare"] = capo_ram.types.resource_share.serialize_json(
            value["resource_share"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateResourceShareResponse:
    out: UpdateResourceShareResponse = {}  # type: ignore[typeddict-item]
    if "resourceShare" in data:
        import capo_ram.types.resource_share

        out["resource_share"] = capo_ram.types.resource_share.deserialize_json(
            data["resourceShare"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
