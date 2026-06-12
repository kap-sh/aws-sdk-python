"""Generated from Smithy shape ``com.amazonaws.healthlake#ProfileConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.default_profiles


class ProfileConfiguration(TypedDict):
    default_profiles: NotRequired[
        "aws_sdk_healthlake.types.default_profiles.DefaultProfiles"
    ]
    """<para>The list of default profiles for the data store.</para>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProfileConfiguration) -> dict:
    out: dict = {}
    if "default_profiles" in value:
        import aws_sdk_healthlake.types.default_profiles

        out["DefaultProfiles"] = (
            aws_sdk_healthlake.types.default_profiles.serialize_aws_json_1_0(
                value["default_profiles"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProfileConfiguration:
    out: ProfileConfiguration = {}  # type: ignore[typeddict-item]
    if "DefaultProfiles" in data:
        import aws_sdk_healthlake.types.default_profiles

        out["default_profiles"] = (
            aws_sdk_healthlake.types.default_profiles.deserialize_aws_json_1_0(
                data["DefaultProfiles"]
            )
        )
    return out
