"""Generated from Smithy shape ``com.amazonaws.lakeformation#CreateLakeFormationOptInRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.condition
    import aws_sdk_lakeformation.types.data_lake_principal
    import aws_sdk_lakeformation.types.resource


class CreateLakeFormationOptInRequest(TypedDict):
    principal: "aws_sdk_lakeformation.types.data_lake_principal.DataLakePrincipal"
    resource: "aws_sdk_lakeformation.types.resource.Resource"
    condition: NotRequired["aws_sdk_lakeformation.types.condition.Condition"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateLakeFormationOptInRequest) -> dict:
    out: dict = {}
    import aws_sdk_lakeformation.types.data_lake_principal

    out["Principal"] = aws_sdk_lakeformation.types.data_lake_principal.serialize_json(
        value["principal"]
    )
    import aws_sdk_lakeformation.types.resource

    out["Resource"] = aws_sdk_lakeformation.types.resource.serialize_json(
        value["resource"]
    )
    if "condition" in value:
        import aws_sdk_lakeformation.types.condition

        out["Condition"] = aws_sdk_lakeformation.types.condition.serialize_json(
            value["condition"]
        )
    return out


def deserialize_json(data: dict) -> CreateLakeFormationOptInRequest:
    out: CreateLakeFormationOptInRequest = {}  # type: ignore[typeddict-item]
    if "Principal" in data:
        import aws_sdk_lakeformation.types.data_lake_principal

        out["principal"] = (
            aws_sdk_lakeformation.types.data_lake_principal.deserialize_json(
                data["Principal"]
            )
        )
    else:
        raise DeserializationError("CreateLakeFormationOptInRequest.principal required")
    if "Resource" in data:
        import aws_sdk_lakeformation.types.resource

        out["resource"] = aws_sdk_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    else:
        raise DeserializationError("CreateLakeFormationOptInRequest.resource required")
    if "Condition" in data:
        import aws_sdk_lakeformation.types.condition

        out["condition"] = aws_sdk_lakeformation.types.condition.deserialize_json(
            data["Condition"]
        )
    return out
