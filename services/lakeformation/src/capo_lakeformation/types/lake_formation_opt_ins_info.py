"""Generated from Smithy shape ``com.amazonaws.lakeformation#LakeFormationOptInsInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.condition
    import capo_lakeformation.types.data_lake_principal
    import capo_lakeformation.types.last_modified_timestamp
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.resource


class LakeFormationOptInsInfo(TypedDict, closed=True):
    resource: NotRequired["capo_lakeformation.types.resource.Resource"]
    principal: NotRequired[
        "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
    ]
    condition: NotRequired["capo_lakeformation.types.condition.Condition"]
    """<p>A Lake Formation condition, which applies to permissions and opt-ins that contain an expression.</p>"""
    last_modified: NotRequired[
        "capo_lakeformation.types.last_modified_timestamp.LastModifiedTimestamp"
    ]
    """<p>The last modified date and time of the record.</p>"""
    last_updated_by: NotRequired["capo_lakeformation.types.name_string.NameString"]
    """<p>The user who updated the record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LakeFormationOptInsInfo) -> dict:
    out: dict = {}
    if "resource" in value:
        import capo_lakeformation.types.resource

        out["Resource"] = capo_lakeformation.types.resource.serialize_json(
            value["resource"]
        )
    if "principal" in value:
        import capo_lakeformation.types.data_lake_principal

        out["Principal"] = capo_lakeformation.types.data_lake_principal.serialize_json(
            value["principal"]
        )
    if "condition" in value:
        import capo_lakeformation.types.condition

        out["Condition"] = capo_lakeformation.types.condition.serialize_json(
            value["condition"]
        )
    if "last_modified" in value:
        import capo_lakeformation.types.last_modified_timestamp

        out["LastModified"] = (
            capo_lakeformation.types.last_modified_timestamp.serialize_json(
                value["last_modified"]
            )
        )
    if "last_updated_by" in value:
        out["LastUpdatedBy"] = value["last_updated_by"]
    return out


def deserialize_json(data: dict) -> LakeFormationOptInsInfo:
    out: LakeFormationOptInsInfo = {}  # type: ignore[typeddict-item]
    if "Resource" in data:
        import capo_lakeformation.types.resource

        out["resource"] = capo_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    if "Principal" in data:
        import capo_lakeformation.types.data_lake_principal

        out["principal"] = (
            capo_lakeformation.types.data_lake_principal.deserialize_json(
                data["Principal"]
            )
        )
    if "Condition" in data:
        import capo_lakeformation.types.condition

        out["condition"] = capo_lakeformation.types.condition.deserialize_json(
            data["Condition"]
        )
    if "LastModified" in data:
        import capo_lakeformation.types.last_modified_timestamp

        out["last_modified"] = (
            capo_lakeformation.types.last_modified_timestamp.deserialize_json(
                data["LastModified"]
            )
        )
    if "LastUpdatedBy" in data:
        out["last_updated_by"] = data["LastUpdatedBy"]
    return out
