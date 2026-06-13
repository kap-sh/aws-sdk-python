"""Generated from Smithy shape ``com.amazonaws.qbusiness#WebExperience``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.timestamp
    import aws_sdk_qbusiness.types.url
    import aws_sdk_qbusiness.types.web_experience_id
    import aws_sdk_qbusiness.types.web_experience_status


class WebExperience(TypedDict):
    web_experience_id: NotRequired[
        "aws_sdk_qbusiness.types.web_experience_id.WebExperienceId"
    ]
    """<p>The identifier of your Amazon Q Business web experience.</p>"""
    created_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business application was last updated.</p>"""
    updated_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when your Amazon Q Business web experience was updated.</p>"""
    default_endpoint: NotRequired["aws_sdk_qbusiness.types.url.Url"]
    """<p>The endpoint URLs for your Amazon Q Business web experience. The URLs are unique and fully hosted by Amazon Web Services.</p>"""
    status: NotRequired[
        "aws_sdk_qbusiness.types.web_experience_status.WebExperienceStatus"
    ]
    """<p>The status of your Amazon Q Business web experience.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebExperience) -> dict:
    out: dict = {}
    if "web_experience_id" in value:
        out["webExperienceId"] = value["web_experience_id"]
    if "created_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["createdAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["updatedAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "default_endpoint" in value:
        out["defaultEndpoint"] = value["default_endpoint"]
    if "status" in value:
        import aws_sdk_qbusiness.types.web_experience_status

        out["status"] = aws_sdk_qbusiness.types.web_experience_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> WebExperience:
    out: WebExperience = {}  # type: ignore[typeddict-item]
    if "webExperienceId" in data:
        out["web_experience_id"] = data["webExperienceId"]
    if "createdAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["created_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["updated_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "defaultEndpoint" in data:
        out["default_endpoint"] = data["defaultEndpoint"]
    if "status" in data:
        import aws_sdk_qbusiness.types.web_experience_status

        out["status"] = aws_sdk_qbusiness.types.web_experience_status.deserialize_json(
            data["status"]
        )
    return out
