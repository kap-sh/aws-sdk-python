"""Generated from Smithy shape ``com.amazonaws.efs#DescribeAccountPreferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_efs.types.resource_id_preference
    import capo_efs.types.token


class DescribeAccountPreferencesResponse(TypedDict, closed=True):
    resource_id_preference: NotRequired[
        "capo_efs.types.resource_id_preference.ResourceIdPreference"
    ]
    """<p>Describes the resource ID preference setting for the Amazon Web Services account associated with the user making the request, in the current Amazon Web Services Region.</p>"""
    next_token: NotRequired["capo_efs.types.token.Token"]
    """<p>Present if there are more records than returned in the response. You can use the <code>NextToken</code> in the subsequent request to fetch the additional descriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccountPreferencesResponse) -> dict:
    out: dict = {}
    if "resource_id_preference" in value:
        import capo_efs.types.resource_id_preference

        out["ResourceIdPreference"] = (
            capo_efs.types.resource_id_preference.serialize_json(
                value["resource_id_preference"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeAccountPreferencesResponse:
    out: DescribeAccountPreferencesResponse = {}  # type: ignore[typeddict-item]
    if "ResourceIdPreference" in data:
        import capo_efs.types.resource_id_preference

        out["resource_id_preference"] = (
            capo_efs.types.resource_id_preference.deserialize_json(
                data["ResourceIdPreference"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
