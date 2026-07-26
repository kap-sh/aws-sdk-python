"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ValidationError``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.business_validation_error
    import capo_partnercentral_account.types.field_validation_error


class _ValidationError_FieldValidationError(TypedDict, closed=True):
    FieldValidationError: (
        "capo_partnercentral_account.types.field_validation_error.FieldValidationError"
    )


class _ValidationError_BusinessValidationError(TypedDict, closed=True):
    BusinessValidationError: "capo_partnercentral_account.types.business_validation_error.BusinessValidationError"


ValidationError: TypeAlias = (
    _ValidationError_FieldValidationError | _ValidationError_BusinessValidationError
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationError) -> dict:
    if "FieldValidationError" in value:
        import capo_partnercentral_account.types.field_validation_error

        return {
            "FieldValidationError": capo_partnercentral_account.types.field_validation_error.serialize_aws_json_1_0(
                value["FieldValidationError"]
            )
        }
    elif "BusinessValidationError" in value:
        import capo_partnercentral_account.types.business_validation_error

        return {
            "BusinessValidationError": capo_partnercentral_account.types.business_validation_error.serialize_aws_json_1_0(
                value["BusinessValidationError"]
            )
        }
    else:
        raise SerializationError("ValidationError: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ValidationError:
    if "FieldValidationError" in data:
        import capo_partnercentral_account.types.field_validation_error

        return {
            "FieldValidationError": capo_partnercentral_account.types.field_validation_error.deserialize_aws_json_1_0(
                data["FieldValidationError"]
            )
        }
    elif "BusinessValidationError" in data:
        import capo_partnercentral_account.types.business_validation_error

        return {
            "BusinessValidationError": capo_partnercentral_account.types.business_validation_error.deserialize_aws_json_1_0(
                data["BusinessValidationError"]
            )
        }
    else:
        raise DeserializationError("ValidationError: no recognized variant key")
