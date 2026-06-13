"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeAutoEnableNewAccountConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.aws_log_source_resource_list
    import aws_sdk_securitylake.types.region


class DataLakeAutoEnableNewAccountConfiguration(TypedDict):
    region: "aws_sdk_securitylake.types.region.Region"
    """<p>The Amazon Web Services Regions where Security Lake is automatically enabled.</p>"""
    sources: "aws_sdk_securitylake.types.aws_log_source_resource_list.AwsLogSourceResourceList"
    """<p>The Amazon Web Services sources that are automatically enabled in Security Lake.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeAutoEnableNewAccountConfiguration) -> dict:
    out: dict = {}
    out["region"] = value["region"]
    import aws_sdk_securitylake.types.aws_log_source_resource_list

    out["sources"] = (
        aws_sdk_securitylake.types.aws_log_source_resource_list.serialize_json(
            value["sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataLakeAutoEnableNewAccountConfiguration:
    out: DataLakeAutoEnableNewAccountConfiguration = {}  # type: ignore[typeddict-item]
    if "region" in data:
        out["region"] = data["region"]
    else:
        raise DeserializationError(
            "DataLakeAutoEnableNewAccountConfiguration.region required"
        )
    if "sources" in data:
        import aws_sdk_securitylake.types.aws_log_source_resource_list

        out["sources"] = (
            aws_sdk_securitylake.types.aws_log_source_resource_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        raise DeserializationError(
            "DataLakeAutoEnableNewAccountConfiguration.sources required"
        )
    return out
