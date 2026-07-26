"""Generated from Smithy shape ``com.amazonaws.healthlake#ProfileConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.default_profiles


class ProfileConfiguration(TypedDict, closed=True):
    default_profiles: NotRequired[
        "capo_healthlake.types.default_profiles.DefaultProfiles"
    ]
    """<para>The list of default profiles for the data store.</para>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProfileConfiguration) -> dict:
    out: dict = {}
    if "default_profiles" in value:
        import capo_healthlake.types.default_profiles

        out["DefaultProfiles"] = (
            capo_healthlake.types.default_profiles.serialize_aws_json_1_0(
                value["default_profiles"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProfileConfiguration:
    out: ProfileConfiguration = {}  # type: ignore[typeddict-item]
    if "DefaultProfiles" in data:
        import capo_healthlake.types.default_profiles

        out["default_profiles"] = (
            capo_healthlake.types.default_profiles.deserialize_aws_json_1_0(
                data["DefaultProfiles"]
            )
        )
    return out
