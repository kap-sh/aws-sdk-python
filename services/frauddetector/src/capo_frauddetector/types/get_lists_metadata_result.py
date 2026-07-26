"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetListsMetadataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.allow_deny_lists
    import capo_frauddetector.types.next_token


class GetListsMetadataResult(TypedDict, closed=True):
    lists: NotRequired["capo_frauddetector.types.allow_deny_lists.AllowDenyLists"]
    """<p> The metadata of the specified list or all lists under the account. </p>"""
    next_token: NotRequired["capo_frauddetector.types.next_token.nextToken"]
    """<p> The next page token. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetListsMetadataResult) -> dict:
    out: dict = {}
    if "lists" in value:
        import capo_frauddetector.types.allow_deny_lists

        out["lists"] = capo_frauddetector.types.allow_deny_lists.serialize_aws_json_1_1(
            value["lists"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetListsMetadataResult:
    out: GetListsMetadataResult = {}  # type: ignore[typeddict-item]
    if "lists" in data:
        import capo_frauddetector.types.allow_deny_lists

        out["lists"] = (
            capo_frauddetector.types.allow_deny_lists.deserialize_aws_json_1_1(
                data["lists"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
