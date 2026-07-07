"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListWebExperiencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.next_token
    import aws_sdk_qbusiness.types.web_experiences


class ListWebExperiencesResponse(TypedDict, closed=True):
    web_experiences: NotRequired[
        "aws_sdk_qbusiness.types.web_experiences.WebExperiences"
    ]
    """<p>An array of summary information for one or more Amazon Q Business experiences.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Q Business returns this token, which you can use in a later request to list the next set of messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWebExperiencesResponse) -> dict:
    out: dict = {}
    if "web_experiences" in value:
        import aws_sdk_qbusiness.types.web_experiences

        out["webExperiences"] = aws_sdk_qbusiness.types.web_experiences.serialize_json(
            value["web_experiences"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWebExperiencesResponse:
    out: ListWebExperiencesResponse = {}  # type: ignore[typeddict-item]
    if "webExperiences" in data:
        import aws_sdk_qbusiness.types.web_experiences

        out["web_experiences"] = (
            aws_sdk_qbusiness.types.web_experiences.deserialize_json(
                data["webExperiences"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
