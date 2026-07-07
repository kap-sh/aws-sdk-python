"""Generated from Smithy shape ``com.amazonaws.opensearch#StorageTypeLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.limit_name
    import aws_sdk_opensearch.types.limit_value_list


class StorageTypeLimit(TypedDict, closed=True):
    limit_name: NotRequired["aws_sdk_opensearch.types.limit_name.LimitName"]
    """<p> Name of storage limits that are applicable for the given storage type. If <code>StorageType</code> is <code>ebs</code>, the following options are available:</p> <ul> <li> <p> <b>MinimumVolumeSize</b> - Minimum volume size that is available for the given storage type. Can be empty if not applicable.</p> </li> <li> <p> <b>MaximumVolumeSize</b> - Maximum volume size that is available for the given storage type. Can be empty if not applicable.</p> </li> <li> <p> <b>MaximumIops</b> - Maximum amount of IOPS that is available for the given the storage type. Can be empty if not applicable.</p> </li> <li> <p> <b>MinimumIops</b> - Minimum amount of IOPS that is available for the given the storage type. Can be empty if not applicable.</p> </li> <li> <p> <b>MaximumThroughput</b> - Maximum amount of throughput that is available for the given the storage type. Can be empty if not applicable.</p> </li> <li> <p> <b>MinimumThroughput</b> - Minimum amount of throughput that is available for the given the storage type. Can be empty if not applicable.</p> </li> </ul>"""
    limit_values: NotRequired[
        "aws_sdk_opensearch.types.limit_value_list.LimitValueList"
    ]
    """<p>The limit values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageTypeLimit) -> dict:
    out: dict = {}
    if "limit_name" in value:
        out["LimitName"] = value["limit_name"]
    if "limit_values" in value:
        import aws_sdk_opensearch.types.limit_value_list

        out["LimitValues"] = aws_sdk_opensearch.types.limit_value_list.serialize_json(
            value["limit_values"]
        )
    return out


def deserialize_json(data: dict) -> StorageTypeLimit:
    out: StorageTypeLimit = {}  # type: ignore[typeddict-item]
    if "LimitName" in data:
        out["limit_name"] = data["LimitName"]
    if "LimitValues" in data:
        import aws_sdk_opensearch.types.limit_value_list

        out["limit_values"] = (
            aws_sdk_opensearch.types.limit_value_list.deserialize_json(
                data["LimitValues"]
            )
        )
    return out
