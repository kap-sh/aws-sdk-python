"""Generated from Smithy shape ``com.amazonaws.kendra#ExperiencesSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.experience_endpoints
    import capo_kendra.types.experience_id
    import capo_kendra.types.experience_name
    import capo_kendra.types.experience_status
    import capo_kendra.types.timestamp


class ExperiencesSummary(TypedDict, closed=True):
    name: NotRequired["capo_kendra.types.experience_name.ExperienceName"]
    """<p>The name of your Amazon Kendra experience.</p>"""
    id: NotRequired["capo_kendra.types.experience_id.ExperienceId"]
    """<p>The identifier of your Amazon Kendra experience.</p>"""
    created_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when your Amazon Kendra experience was created.</p>"""
    status: NotRequired["capo_kendra.types.experience_status.ExperienceStatus"]
    """<p>The processing status of your Amazon Kendra experience.</p>"""
    endpoints: NotRequired["capo_kendra.types.experience_endpoints.ExperienceEndpoints"]
    """<p>The endpoint URLs for your Amazon Kendra experiences. The URLs are unique and fully hosted by Amazon Web Services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperiencesSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "created_at" in value:
        import capo_kendra.types.timestamp

        out["CreatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "status" in value:
        import capo_kendra.types.experience_status

        out["Status"] = capo_kendra.types.experience_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "endpoints" in value:
        import capo_kendra.types.experience_endpoints

        out["Endpoints"] = (
            capo_kendra.types.experience_endpoints.serialize_aws_json_1_1(
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
        import capo_kendra.types.timestamp

        out["created_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "Status" in data:
        import capo_kendra.types.experience_status

        out["status"] = capo_kendra.types.experience_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Endpoints" in data:
        import capo_kendra.types.experience_endpoints

        out["endpoints"] = (
            capo_kendra.types.experience_endpoints.deserialize_aws_json_1_1(
                data["Endpoints"]
            )
        )
    return out
