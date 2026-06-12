"""Generated from Smithy shape ``com.amazonaws.kendra#ExperiencesSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.experience_endpoints
    import aws_sdk_kendra.types.experience_id
    import aws_sdk_kendra.types.experience_name
    import aws_sdk_kendra.types.experience_status
    import aws_sdk_kendra.types.timestamp


class ExperiencesSummary(TypedDict):
    name: NotRequired["aws_sdk_kendra.types.experience_name.ExperienceName"]
    """<p>The name of your Amazon Kendra experience.</p>"""
    id: NotRequired["aws_sdk_kendra.types.experience_id.ExperienceId"]
    """<p>The identifier of your Amazon Kendra experience.</p>"""
    created_at: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when your Amazon Kendra experience was created.</p>"""
    status: NotRequired["aws_sdk_kendra.types.experience_status.ExperienceStatus"]
    """<p>The processing status of your Amazon Kendra experience.</p>"""
    endpoints: NotRequired[
        "aws_sdk_kendra.types.experience_endpoints.ExperienceEndpoints"
    ]
    """<p>The endpoint URLs for your Amazon Kendra experiences. The URLs are unique and fully hosted by Amazon Web Services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperiencesSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "created_at" in value:
        import aws_sdk_kendra.types.timestamp

        out["CreatedAt"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "status" in value:
        import aws_sdk_kendra.types.experience_status

        out["Status"] = aws_sdk_kendra.types.experience_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "endpoints" in value:
        import aws_sdk_kendra.types.experience_endpoints

        out["Endpoints"] = (
            aws_sdk_kendra.types.experience_endpoints.serialize_aws_json_1_1(
                value["endpoints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExperiencesSummary:
    out: ExperiencesSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "CreatedAt" in data:
        import aws_sdk_kendra.types.timestamp

        out["created_at"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "Status" in data:
        import aws_sdk_kendra.types.experience_status

        out["status"] = aws_sdk_kendra.types.experience_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Endpoints" in data:
        import aws_sdk_kendra.types.experience_endpoints

        out["endpoints"] = (
            aws_sdk_kendra.types.experience_endpoints.deserialize_aws_json_1_1(
                data["Endpoints"]
            )
        )
    return out
