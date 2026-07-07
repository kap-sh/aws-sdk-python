"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetDelegationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.delegation_metadata_list
    import aws_sdk_auditmanager.types.token


class GetDelegationsResponse(TypedDict, closed=True):
    delegations: NotRequired[
        "aws_sdk_auditmanager.types.delegation_metadata_list.DelegationMetadataList"
    ]
    """<p> The list of delegations that the <code>GetDelegations</code> API returned. </p>"""
    next_token: NotRequired["aws_sdk_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDelegationsResponse) -> dict:
    out: dict = {}
    if "delegations" in value:
        import aws_sdk_auditmanager.types.delegation_metadata_list

        out["delegations"] = (
            aws_sdk_auditmanager.types.delegation_metadata_list.serialize_json(
                value["delegations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetDelegationsResponse:
    out: GetDelegationsResponse = {}  # type: ignore[typeddict-item]
    if "delegations" in data:
        import aws_sdk_auditmanager.types.delegation_metadata_list

        out["delegations"] = (
            aws_sdk_auditmanager.types.delegation_metadata_list.deserialize_json(
                data["delegations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
