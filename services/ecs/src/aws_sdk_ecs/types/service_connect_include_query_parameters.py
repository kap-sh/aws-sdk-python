"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectIncludeQueryParameters``."""

from typing import Literal, TypeAlias, cast

"""<p>Controls whether query parameters are included in Service Connect access logs. Consider security and privacy implications when enabling this feature. By default, this parameter is <code>DISABLED</code>.</p>"""
ServiceConnectIncludeQueryParameters: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectIncludeQueryParameters) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceConnectIncludeQueryParameters:
    return cast(ServiceConnectIncludeQueryParameters, data)
