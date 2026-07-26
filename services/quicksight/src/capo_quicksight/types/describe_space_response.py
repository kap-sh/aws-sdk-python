"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeSpaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.public_space_arn
    import capo_quicksight.types.public_space_id
    import capo_quicksight.types.space_contributor_list
    import capo_quicksight.types.space_details


class DescribeSpaceResponse(TypedDict, closed=True):
    space_id: "capo_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space.</p>"""
    space_arn: NotRequired["capo_quicksight.types.public_space_arn.PublicSpaceArn"]
    """<p>The ARN of the space.</p>"""
    space: "capo_quicksight.types.space_details.SpaceDetails"
    """<p>The details of the space.</p>"""
    contributors: NotRequired[
        "capo_quicksight.types.space_contributor_list.SpaceContributorList"
    ]
    """<p>A list of contributors to the space.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSpaceResponse) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "space_arn" in value:
        out["spaceArn"] = value["space_arn"]
    import capo_quicksight.types.space_details

    out["Space"] = capo_quicksight.types.space_details.serialize_json(value["space"])
    if "contributors" in value:
        import capo_quicksight.types.space_contributor_list

        out["Contributors"] = (
            capo_quicksight.types.space_contributor_list.serialize_json(
                value["contributors"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeSpaceResponse:
    out: DescribeSpaceResponse = {}  # type: ignore[typeddict-item]
    if "spaceId" in data:
        out["space_id"] = data["spaceId"]
    else:
        raise DeserializationError("DescribeSpaceResponse.space_id required")
    if "spaceArn" in data:
        out["space_arn"] = data["spaceArn"]
    if "Space" in data:
        import capo_quicksight.types.space_details

        out["space"] = capo_quicksight.types.space_details.deserialize_json(
            data["Space"]
        )
    else:
        raise DeserializationError("DescribeSpaceResponse.space required")
    if "Contributors" in data:
        import capo_quicksight.types.space_contributor_list

        out["contributors"] = (
            capo_quicksight.types.space_contributor_list.deserialize_json(
                data["Contributors"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
