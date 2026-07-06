"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#StorageTypeLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.limit_name
    import aws_sdk_elasticsearch_service.types.limit_value_list


class StorageTypeLimit(TypedDict, closed=True):
    limit_name: NotRequired["aws_sdk_elasticsearch_service.types.limit_name.LimitName"]
    """<p> Name of storage limits that are applicable for given storage type. If <code> <a>StorageType</a> </code> is ebs, following storage options are applicable <ol> <li>MinimumVolumeSize</li> Minimum amount of volume size that is applicable for given storage type.It can be empty if it is not applicable. <li>MaximumVolumeSize</li> Maximum amount of volume size that is applicable for given storage type.It can be empty if it is not applicable. <li>MaximumIops</li> Maximum amount of Iops that is applicable for given storage type.It can be empty if it is not applicable. <li>MinimumIops</li> Minimum amount of Iops that is applicable for given storage type.It can be empty if it is not applicable. <li>MaximumThroughput</li> Maximum amount of Throughput that is applicable for given storage type.It can be empty if it is not applicable. <li>MinimumThroughput</li> Minimum amount of Throughput that is applicable for given storage type.It can be empty if it is not applicable. </ol> </p>"""
    limit_values: NotRequired[
        "aws_sdk_elasticsearch_service.types.limit_value_list.LimitValueList"
    ]
    """<p> Values for the <code> <a>StorageTypeLimit$LimitName</a> </code> . </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageTypeLimit) -> dict:
    out: dict = {}
    if "limit_name" in value:
        out["LimitName"] = value["limit_name"]
    if "limit_values" in value:
        import aws_sdk_elasticsearch_service.types.limit_value_list

        out["LimitValues"] = (
            aws_sdk_elasticsearch_service.types.limit_value_list.serialize_json(
                value["limit_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> StorageTypeLimit:
    out: StorageTypeLimit = {}  # type: ignore[typeddict-item]
    if "LimitName" in data:
        out["limit_name"] = data["LimitName"]
    if "LimitValues" in data:
        import aws_sdk_elasticsearch_service.types.limit_value_list

        out["limit_values"] = (
            aws_sdk_elasticsearch_service.types.limit_value_list.deserialize_json(
                data["LimitValues"]
            )
        )
    return out
