"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListRotationOverridesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.pagination_token
    import capo_ssm_contacts.types.rotation_overrides


class ListRotationOverridesResult(TypedDict, closed=True):
    rotation_overrides: NotRequired[
        "capo_ssm_contacts.types.rotation_overrides.RotationOverrides"
    ]
    """<p>A list of rotation overrides in the specified time range.</p>"""
    next_token: NotRequired["capo_ssm_contacts.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRotationOverridesResult) -> dict:
    out: dict = {}
    if "rotation_overrides" in value:
        import capo_ssm_contacts.types.rotation_overrides

        out["RotationOverrides"] = (
            capo_ssm_contacts.types.rotation_overrides.serialize_aws_json_1_1(
                value["rotation_overrides"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRotationOverridesResult:
    out: ListRotationOverridesResult = {}  # type: ignore[typeddict-item]
    if "RotationOverrides" in data:
        import capo_ssm_contacts.types.rotation_overrides

        out["rotation_overrides"] = (
            capo_ssm_contacts.types.rotation_overrides.deserialize_aws_json_1_1(
                data["RotationOverrides"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
