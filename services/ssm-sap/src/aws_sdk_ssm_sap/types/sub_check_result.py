"""Generated from Smithy shape ``com.amazonaws.ssmsap#SubCheckResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.sub_check_references_list
    import aws_sdk_ssm_sap.types.sub_check_result_id


class SubCheckResult(TypedDict):
    id: NotRequired["aws_sdk_ssm_sap.types.sub_check_result_id.SubCheckResultId"]
    """<p>The unique identifier of the sub-check result.</p>"""
    name: NotRequired["str"]
    """<p>The name of the sub-check.</p>"""
    description: NotRequired["str"]
    """<p>A description of what the sub-check validates.</p>"""
    references: NotRequired[
        "aws_sdk_ssm_sap.types.sub_check_references_list.SubCheckReferencesList"
    ]
    """<p>A list of references or documentation links related to the sub-check.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubCheckResult) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "references" in value:
        import aws_sdk_ssm_sap.types.sub_check_references_list

        out["References"] = (
            aws_sdk_ssm_sap.types.sub_check_references_list.serialize_json(
                value["references"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubCheckResult:
    out: SubCheckResult = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "References" in data:
        import aws_sdk_ssm_sap.types.sub_check_references_list

        out["references"] = (
            aws_sdk_ssm_sap.types.sub_check_references_list.deserialize_json(
                data["References"]
            )
        )
    return out
