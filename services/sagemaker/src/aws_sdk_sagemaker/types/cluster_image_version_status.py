"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterImageVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

"""<p>The status of the Amazon Machine Image (AMI) version for the HyperPod cluster instance group, node, or cluster. The AMI version is determined at the instance group level, and all nodes within an instance group run the same AMI. The cluster-level status is aggregated across all instance groups.</p> <ul> <li> <p> <code>UpToDate</code>: The resource is running the latest available AMI version.</p> </li> <li> <p> <code>UpdateAvailable</code>: A newer AMI version is available for the resource.</p> </li> </ul>"""
ClusterImageVersionStatus: TypeAlias = Literal[
    "UpToDate",
    "UpdateAvailable",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UpToDate",
        "UpdateAvailable",
    )
)


def serialize_aws_json_1_1(value: ClusterImageVersionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterImageVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterImageVersionStatus value: {data!r}")
    return cast(ClusterImageVersionStatus, data)
