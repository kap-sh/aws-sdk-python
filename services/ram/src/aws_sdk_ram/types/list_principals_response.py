"""Generated from Smithy shape ``com.amazonaws.ram#ListPrincipalsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.principal_list
    import aws_sdk_ram.types.string


class ListPrincipalsResponse(TypedDict):
    principals: NotRequired["aws_sdk_ram.types.principal_list.PrincipalList"]
    """<p>An array of objects that contain the details about the principals.</p>"""
    next_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrincipalsResponse) -> dict:
    out: dict = {}
    if "principals" in value:
        import aws_sdk_ram.types.principal_list

        out["principals"] = aws_sdk_ram.types.principal_list.serialize_json(
            value["principals"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPrincipalsResponse:
    out: ListPrincipalsResponse = {}  # type: ignore[typeddict-item]
    if "principals" in data:
        import aws_sdk_ram.types.principal_list

        out["principals"] = aws_sdk_ram.types.principal_list.deserialize_json(
            data["principals"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
