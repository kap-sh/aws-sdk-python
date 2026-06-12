"""Generated from Smithy shape ``com.amazonaws.identitystore#IsMemberInGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.group_membership_existence_results


class IsMemberInGroupsResponse(TypedDict):
    results: "aws_sdk_identitystore.types.group_membership_existence_results.GroupMembershipExistenceResults"
    """<p>A list containing the results of membership existence checks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IsMemberInGroupsResponse) -> dict:
    out: dict = {}
    import aws_sdk_identitystore.types.group_membership_existence_results

    out["Results"] = (
        aws_sdk_identitystore.types.group_membership_existence_results.serialize_aws_json_1_1(
            value["results"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IsMemberInGroupsResponse:
    out: IsMemberInGroupsResponse = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_identitystore.types.group_membership_existence_results

        out["results"] = (
            aws_sdk_identitystore.types.group_membership_existence_results.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    else:
        raise DeserializationError("IsMemberInGroupsResponse.results required")
    return out
