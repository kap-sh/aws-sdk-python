"""Generated from Smithy shape ``com.amazonaws.snowball#DependentService``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.service_name
    import aws_sdk_snowball.types.service_version


class DependentService(TypedDict):
    service_name: NotRequired["aws_sdk_snowball.types.service_name.ServiceName"]
    """<p>The name of the dependent service.</p>"""
    service_version: NotRequired[
        "aws_sdk_snowball.types.service_version.ServiceVersion"
    ]
    """<p>The version of the dependent service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DependentService) -> dict:
    out: dict = {}
    if "service_name" in value:
        import aws_sdk_snowball.types.service_name

        out["ServiceName"] = aws_sdk_snowball.types.service_name.serialize_aws_json_1_1(
            value["service_name"]
        )
    if "service_version" in value:
        import aws_sdk_snowball.types.service_version

        out["ServiceVersion"] = (
            aws_sdk_snowball.types.service_version.serialize_aws_json_1_1(
                value["service_version"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DependentService:
    out: DependentService = {}  # type: ignore[typeddict-item]
    if "ServiceName" in data:
        import aws_sdk_snowball.types.service_name

        out["service_name"] = (
            aws_sdk_snowball.types.service_name.deserialize_aws_json_1_1(
                data["ServiceName"]
            )
        )
    if "ServiceVersion" in data:
        import aws_sdk_snowball.types.service_version

        out["service_version"] = (
            aws_sdk_snowball.types.service_version.deserialize_aws_json_1_1(
                data["ServiceVersion"]
            )
        )
    return out
