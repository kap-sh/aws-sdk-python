"""Generated from Smithy shape ``com.amazonaws.identitystore#IsMemberInGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.group_membership_existence_results


class IsMemberInGroupsResponse(TypedDict, closed=True):
    results: "capo_identitystore.types.group_membership_existence_results.GroupMembershipExistenceResults"
    """<p>A list containing the results of membership existence checks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IsMemberInGroupsResponse) -> dict:
    out: dict = {}
    import capo_identitystore.types.group_membership_existence_results

    out["Results"] = (
        capo_identitystore.types.group_membership_existence_results.serialize_aws_json_1_1(
            value["results"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IsMemberInGroupsResponse:
    out: IsMemberInGroupsResponse = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import capo_identitystore.types.group_membership_existence_results

        out["results"] = (
            capo_identitystore.types.group_membership_existence_results.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    else:
        raise DeserializationError("IsMemberInGroupsResponse.results required")
    return out
