"""Generated from Smithy shape ``com.amazonaws.fsx#ServiceLimit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

"""<p>The types of limits on your service utilization. Limits include file system count, total throughput capacity, total storage, and total user-initiated backups. These limits apply for a specific account in a specific Amazon Web Services Region. You can increase some of them by contacting Amazon Web Services Support.</p>"""
ServiceLimit: TypeAlias = Literal[
    "FILE_SYSTEM_COUNT",
    "TOTAL_THROUGHPUT_CAPACITY",
    "TOTAL_STORAGE",
    "TOTAL_USER_INITIATED_BACKUPS",
    "TOTAL_USER_TAGS",
    "TOTAL_IN_PROGRESS_COPY_BACKUPS",
    "STORAGE_VIRTUAL_MACHINES_PER_FILE_SYSTEM",
    "VOLUMES_PER_FILE_SYSTEM",
    "TOTAL_SSD_IOPS",
    "FILE_CACHE_COUNT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FILE_SYSTEM_COUNT",
        "TOTAL_THROUGHPUT_CAPACITY",
        "TOTAL_STORAGE",
        "TOTAL_USER_INITIATED_BACKUPS",
        "TOTAL_USER_TAGS",
        "TOTAL_IN_PROGRESS_COPY_BACKUPS",
        "STORAGE_VIRTUAL_MACHINES_PER_FILE_SYSTEM",
        "VOLUMES_PER_FILE_SYSTEM",
        "TOTAL_SSD_IOPS",
        "FILE_CACHE_COUNT",
    )
)


def serialize_aws_json_1_1(value: ServiceLimit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceLimit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceLimit value: {data!r}")
    return cast(ServiceLimit, data)
