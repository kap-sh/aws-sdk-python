"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListInstanceProfilesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.instance_profiles
    import aws_sdk_device_farm.types.pagination_token


class ListInstanceProfilesResult(TypedDict):
    instance_profiles: NotRequired[
        "aws_sdk_device_farm.types.instance_profiles.InstanceProfiles"
    ]
    """<p>An object that contains information about your instance profiles.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>An identifier that can be used in the next call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInstanceProfilesResult) -> dict:
    out: dict = {}
    if "instance_profiles" in value:
        import aws_sdk_device_farm.types.instance_profiles

        out["instanceProfiles"] = (
            aws_sdk_device_farm.types.instance_profiles.serialize_aws_json_1_1(
                value["instance_profiles"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInstanceProfilesResult:
    out: ListInstanceProfilesResult = {}  # type: ignore[typeddict-item]
    if "instanceProfiles" in data:
        import aws_sdk_device_farm.types.instance_profiles

        out["instance_profiles"] = (
            aws_sdk_device_farm.types.instance_profiles.deserialize_aws_json_1_1(
                data["instanceProfiles"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
