"""Generated from Smithy shape ``com.amazonaws.kendra#ThesaurusSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.thesaurus_id
    import capo_kendra.types.thesaurus_name
    import capo_kendra.types.thesaurus_status
    import capo_kendra.types.timestamp


class ThesaurusSummary(TypedDict, closed=True):
    id: NotRequired["capo_kendra.types.thesaurus_id.ThesaurusId"]
    """<p>The identifier of the thesaurus.</p>"""
    name: NotRequired["capo_kendra.types.thesaurus_name.ThesaurusName"]
    """<p>The name of the thesaurus.</p>"""
    status: NotRequired["capo_kendra.types.thesaurus_status.ThesaurusStatus"]
    """<p>The status of the thesaurus.</p>"""
    created_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the thesaurus was created.</p>"""
    updated_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the thesaurus was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThesaurusSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_kendra.types.thesaurus_status

        out["Status"] = capo_kendra.types.thesaurus_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "created_at" in value:
        import capo_kendra.types.timestamp

        out["CreatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_kendra.types.timestamp

        out["UpdatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ThesaurusSummary:
    out: ThesaurusSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import capo_kendra.types.thesaurus_status

        out["status"] = capo_kendra.types.thesaurus_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "CreatedAt" in data:
        import capo_kendra.types.timestamp

        out["created_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import capo_kendra.types.timestamp

        out["updated_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    return out
