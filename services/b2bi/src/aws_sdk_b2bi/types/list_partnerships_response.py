"""Generated from Smithy shape ``com.amazonaws.b2bi#ListPartnershipsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.page_token
    import aws_sdk_b2bi.types.partnership_list


class ListPartnershipsResponse(TypedDict, closed=True):
    partnerships: "aws_sdk_b2bi.types.partnership_list.PartnershipList"
    """<p>Specifies a list of your partnerships.</p>"""
    next_token: NotRequired["aws_sdk_b2bi.types.page_token.PageToken"]
    """<p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPartnershipsResponse) -> dict:
    out: dict = {}
    import aws_sdk_b2bi.types.partnership_list

    out["partnerships"] = aws_sdk_b2bi.types.partnership_list.serialize_aws_json_1_0(
        value["partnerships"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPartnershipsResponse:
    out: ListPartnershipsResponse = {}  # type: ignore[typeddict-item]
    if "partnerships" in data:
        import aws_sdk_b2bi.types.partnership_list

        out["partnerships"] = (
            aws_sdk_b2bi.types.partnership_list.deserialize_aws_json_1_0(
                data["partnerships"]
            )
        )
    else:
        raise DeserializationError("ListPartnershipsResponse.partnerships required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
