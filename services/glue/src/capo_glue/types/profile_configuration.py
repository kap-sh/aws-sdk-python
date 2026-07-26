"""Generated from Smithy shape ``com.amazonaws.glue#ProfileConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.configuration_map


class ProfileConfiguration(TypedDict, closed=True):
    session_configuration: NotRequired[
        "capo_glue.types.configuration_map.ConfigurationMap"
    ]
    """<p>A key-value map of configuration parameters for Glue sessions. </p>"""
    job_configuration: NotRequired["capo_glue.types.configuration_map.ConfigurationMap"]
    """<p>A key-value map of configuration parameters for Glue jobs. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProfileConfiguration) -> dict:
    out: dict = {}
    if "session_configuration" in value:
        import capo_glue.types.configuration_map

        out["SessionConfiguration"] = (
            capo_glue.types.configuration_map.serialize_aws_json_1_1(
                value["session_configuration"]
            )
        )
    if "job_configuration" in value:
        import capo_glue.types.configuration_map

        out["JobConfiguration"] = (
            capo_glue.types.configuration_map.serialize_aws_json_1_1(
                value["job_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProfileConfiguration:
    out: ProfileConfiguration = {}  # type: ignore[typeddict-item]
    if "SessionConfiguration" in data:
        import capo_glue.types.configuration_map

        out["session_configuration"] = (
            capo_glue.types.configuration_map.deserialize_aws_json_1_1(
                data["SessionConfiguration"]
            )
        )
    if "JobConfiguration" in data:
        import capo_glue.types.configuration_map

        out["job_configuration"] = (
            capo_glue.types.configuration_map.deserialize_aws_json_1_1(
                data["JobConfiguration"]
            )
        )
    return out
