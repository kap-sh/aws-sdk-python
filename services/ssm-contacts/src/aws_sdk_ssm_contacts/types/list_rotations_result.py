"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListRotationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.pagination_token
    import aws_sdk_ssm_contacts.types.rotations


class ListRotationsResult(TypedDict):
    next_token: NotRequired[
        "aws_sdk_ssm_contacts.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""
    rotations: "aws_sdk_ssm_contacts.types.rotations.Rotations"
    """<p>Information about rotations that meet the filter criteria.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRotationsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_ssm_contacts.types.rotations

    out["Rotations"] = aws_sdk_ssm_contacts.types.rotations.serialize_aws_json_1_1(
        value["rotations"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRotationsResult:
    out: ListRotationsResult = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Rotations" in data:
        import aws_sdk_ssm_contacts.types.rotations

        out["rotations"] = (
            aws_sdk_ssm_contacts.types.rotations.deserialize_aws_json_1_1(
                data["Rotations"]
            )
        )
    else:
        raise DeserializationError("ListRotationsResult.rotations required")
    return out
