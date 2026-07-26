"""Generated from Smithy shape ``com.amazonaws.datazone#LakeFormationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.role_arn
    import capo_datazone.types.s3_location_list


class LakeFormationConfiguration(TypedDict, closed=True):
    location_registration_role: NotRequired["capo_datazone.types.role_arn.RoleArn"]
    """<p>The role that is used to manage read/write access to the chosen Amazon S3 bucket(s) for Data Lake using Amazon Web Services Lake Formation hybrid access mode.</p>"""
    location_registration_exclude_s3_locations: NotRequired[
        "capo_datazone.types.s3_location_list.S3LocationList"
    ]
    """<p>Specifies certain Amazon S3 locations if you do not want Amazon DataZone to automatically register them in hybrid mode. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LakeFormationConfiguration) -> dict:
    out: dict = {}
    if "location_registration_role" in value:
        out["locationRegistrationRole"] = value["location_registration_role"]
    if "location_registration_exclude_s3_locations" in value:
        import capo_datazone.types.s3_location_list

        out["locationRegistrationExcludeS3Locations"] = (
            capo_datazone.types.s3_location_list.serialize_json(
                value["location_registration_exclude_s3_locations"]
            )
        )
    return out


def deserialize_json(data: dict) -> LakeFormationConfiguration:
    out: LakeFormationConfiguration = {}  # type: ignore[typeddict-item]
    if "locationRegistrationRole" in data:
        out["location_registration_role"] = data["locationRegistrationRole"]
    if "locationRegistrationExcludeS3Locations" in data:
        import capo_datazone.types.s3_location_list

        out["location_registration_exclude_s3_locations"] = (
            capo_datazone.types.s3_location_list.deserialize_json(
                data["locationRegistrationExcludeS3Locations"]
            )
        )
    return out
