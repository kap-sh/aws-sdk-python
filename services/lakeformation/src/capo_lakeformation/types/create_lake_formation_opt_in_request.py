"""Generated from Smithy shape ``com.amazonaws.lakeformation#CreateLakeFormationOptInRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.condition
    import capo_lakeformation.types.data_lake_principal
    import capo_lakeformation.types.resource


class CreateLakeFormationOptInRequest(TypedDict, closed=True):
    principal: "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
    resource: "capo_lakeformation.types.resource.Resource"
    condition: NotRequired["capo_lakeformation.types.condition.Condition"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateLakeFormationOptInRequest) -> dict:
    out: dict = {}
    import capo_lakeformation.types.data_lake_principal

    out["Principal"] = capo_lakeformation.types.data_lake_principal.serialize_json(
        value["principal"]
    )
    import capo_lakeformation.types.resource

    out["Resource"] = capo_lakeformation.types.resource.serialize_json(
        value["resource"]
    )
    if "condition" in value:
        import capo_lakeformation.types.condition

        out["Condition"] = capo_lakeformation.types.condition.serialize_json(
            value["condition"]
        )
    return out


def deserialize_json(data: dict) -> CreateLakeFormationOptInRequest:
    out: CreateLakeFormationOptInRequest = {}  # type: ignore[typeddict-item]
    if "Principal" in data:
        import capo_lakeformation.types.data_lake_principal

        out["principal"] = (
            capo_lakeformation.types.data_lake_principal.deserialize_json(
                data["Principal"]
            )
        )
    else:
        raise DeserializationError("CreateLakeFormationOptInRequest.principal required")
    if "Resource" in data:
        import capo_lakeformation.types.resource

        out["resource"] = capo_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    else:
        raise DeserializationError("CreateLakeFormationOptInRequest.resource required")
    if "Condition" in data:
        import capo_lakeformation.types.condition

        out["condition"] = capo_lakeformation.types.condition.deserialize_json(
            data["Condition"]
        )
    return out
