"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterEventLevel``."""

from typing import Literal, TypeAlias, cast

"""<p>The severity level for a HyperPod cluster event.</p>"""
ClusterEventLevel: TypeAlias = Literal[
    "Info",
    "Warn",
    "Error",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterEventLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterEventLevel:
    return cast(ClusterEventLevel, data)
