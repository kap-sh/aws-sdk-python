"""Generated from Smithy shape ``com.amazonaws.datazone#SelfGrantStatusOutput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.glue_self_grant_status_output
    import aws_sdk_datazone.types.redshift_self_grant_status_output


class _SelfGrantStatusOutput_glueSelfGrantStatus(TypedDict):
    glueSelfGrantStatus: (
        "aws_sdk_datazone.types.glue_self_grant_status_output.GlueSelfGrantStatusOutput"
    )


class _SelfGrantStatusOutput_redshiftSelfGrantStatus(TypedDict):
    redshiftSelfGrantStatus: "aws_sdk_datazone.types.redshift_self_grant_status_output.RedshiftSelfGrantStatusOutput"


SelfGrantStatusOutput: TypeAlias = (
    _SelfGrantStatusOutput_glueSelfGrantStatus
    | _SelfGrantStatusOutput_redshiftSelfGrantStatus
)


# --- restJson1 ser/de ---
def serialize_json(value: SelfGrantStatusOutput) -> dict:
    if "glueSelfGrantStatus" in value:
        import aws_sdk_datazone.types.glue_self_grant_status_output

        return {
            "glueSelfGrantStatus": aws_sdk_datazone.types.glue_self_grant_status_output.serialize_json(
                value["glueSelfGrantStatus"]
            )
        }
    elif "redshiftSelfGrantStatus" in value:
        import aws_sdk_datazone.types.redshift_self_grant_status_output

        return {
            "redshiftSelfGrantStatus": aws_sdk_datazone.types.redshift_self_grant_status_output.serialize_json(
                value["redshiftSelfGrantStatus"]
            )
        }
    else:
        raise SerializationError("SelfGrantStatusOutput: no variant present")


def deserialize_json(data: dict) -> SelfGrantStatusOutput:
    if "glueSelfGrantStatus" in data:
        import aws_sdk_datazone.types.glue_self_grant_status_output

        return {
            "glueSelfGrantStatus": aws_sdk_datazone.types.glue_self_grant_status_output.deserialize_json(
                data["glueSelfGrantStatus"]
            )
        }
    elif "redshiftSelfGrantStatus" in data:
        import aws_sdk_datazone.types.redshift_self_grant_status_output

        return {
            "redshiftSelfGrantStatus": aws_sdk_datazone.types.redshift_self_grant_status_output.deserialize_json(
                data["redshiftSelfGrantStatus"]
            )
        }
    else:
        raise DeserializationError("SelfGrantStatusOutput: no recognized variant key")
