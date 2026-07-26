"""Generated from Smithy shape ``com.amazonaws.datazone#SelfGrantStatusOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.glue_self_grant_status_output
    import capo_datazone.types.redshift_self_grant_status_output


class _SelfGrantStatusOutput_glueSelfGrantStatus(TypedDict, closed=True):
    glueSelfGrantStatus: (
        "capo_datazone.types.glue_self_grant_status_output.GlueSelfGrantStatusOutput"
    )


class _SelfGrantStatusOutput_redshiftSelfGrantStatus(TypedDict, closed=True):
    redshiftSelfGrantStatus: "capo_datazone.types.redshift_self_grant_status_output.RedshiftSelfGrantStatusOutput"


SelfGrantStatusOutput: TypeAlias = (
    _SelfGrantStatusOutput_glueSelfGrantStatus
    | _SelfGrantStatusOutput_redshiftSelfGrantStatus
)


# --- restJson1 ser/de ---
def serialize_json(value: SelfGrantStatusOutput) -> dict:
    if "glueSelfGrantStatus" in value:
        import capo_datazone.types.glue_self_grant_status_output

        return {
            "glueSelfGrantStatus": capo_datazone.types.glue_self_grant_status_output.serialize_json(
                value["glueSelfGrantStatus"]
            )
        }
    elif "redshiftSelfGrantStatus" in value:
        import capo_datazone.types.redshift_self_grant_status_output

        return {
            "redshiftSelfGrantStatus": capo_datazone.types.redshift_self_grant_status_output.serialize_json(
                value["redshiftSelfGrantStatus"]
            )
        }
    else:
        raise SerializationError("SelfGrantStatusOutput: no variant present")


def deserialize_json(data: dict) -> SelfGrantStatusOutput:
    if "glueSelfGrantStatus" in data:
        import capo_datazone.types.glue_self_grant_status_output

        return {
            "glueSelfGrantStatus": capo_datazone.types.glue_self_grant_status_output.deserialize_json(
                data["glueSelfGrantStatus"]
            )
        }
    elif "redshiftSelfGrantStatus" in data:
        import capo_datazone.types.redshift_self_grant_status_output

        return {
            "redshiftSelfGrantStatus": capo_datazone.types.redshift_self_grant_status_output.deserialize_json(
                data["redshiftSelfGrantStatus"]
            )
        }
    else:
        raise DeserializationError("SelfGrantStatusOutput: no recognized variant key")
