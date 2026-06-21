"""Generated from Smithy shape ``com.amazonaws.sagemaker#HomeEfsFileSystemCreation``."""

from typing import Literal, TypeAlias, cast

"""<p>Indicates whether a home EFS file system is created for the domain.</p>"""
HomeEfsFileSystemCreation: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HomeEfsFileSystemCreation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HomeEfsFileSystemCreation:
    return cast(HomeEfsFileSystemCreation, data)
