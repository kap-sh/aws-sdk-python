"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ListRecoveryGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__list_of_recovery_group_output
    import aws_sdk_route53_recovery_readiness.types.__string


class ListRecoveryGroupsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    recovery_groups: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__list_of_recovery_group_output.__listOfRecoveryGroupOutput"
    ]
    """<p>A list of recovery groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecoveryGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "recovery_groups" in value:
        import aws_sdk_route53_recovery_readiness.types.__list_of_recovery_group_output

        out["recoveryGroups"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_recovery_group_output.serialize_json(
                value["recovery_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRecoveryGroupsResponse:
    out: ListRecoveryGroupsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "recoveryGroups" in data:
        import aws_sdk_route53_recovery_readiness.types.__list_of_recovery_group_output

        out["recovery_groups"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_recovery_group_output.deserialize_json(
                data["recoveryGroups"]
            )
        )
    return out
