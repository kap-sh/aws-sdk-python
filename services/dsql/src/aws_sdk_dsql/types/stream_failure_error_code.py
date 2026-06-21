"""Generated from Smithy shape ``com.amazonaws.dsql#StreamFailureErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>Error codes for stream failures.</p> <dl> <dt>KINESIS_THROUGHPUT_EXCEEDED</dt> <dd> <p>The Kinesis stream throughput limit was exceeded.</p> </dd> <dt>KINESIS_STREAM_NOT_FOUND</dt> <dd> <p>The specified Kinesis stream was not found.</p> </dd> <dt>ROLE_ACCESS_DENIED</dt> <dd> <p>Access was denied for the specified IAM role.</p> </dd> <dt>KINESIS_ACCESS_DENIED</dt> <dd> <p>Access to the Kinesis stream was denied.</p> </dd> <dt>KINESIS_KMS_ACCESS_DENIED</dt> <dd> <p>Access to the KMS key for the Kinesis stream was denied.</p> </dd> <dt>KINESIS_OVERSIZE_RECORD</dt> <dd> <p>A record exceeded the Kinesis stream size limit.</p> </dd> <dt>CLUSTER_CMK_INACCESSIBLE</dt> <dd> <p>The cluster's customer-managed key is inaccessible.</p> </dd> <dt>INTERNAL_ERROR</dt> <dd> <p>An internal error occurred.</p> </dd> </dl>"""
StreamFailureErrorCode: TypeAlias = Literal[
    "KINESIS_THROUGHPUT_EXCEEDED",
    "KINESIS_STREAM_NOT_FOUND",
    "ROLE_ACCESS_DENIED",
    "KINESIS_ACCESS_DENIED",
    "KINESIS_KMS_ACCESS_DENIED",
    "KINESIS_OVERSIZE_RECORD",
    "CLUSTER_CMK_INACCESSIBLE",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamFailureErrorCode) -> str:
    return value


def deserialize_json(data: str) -> StreamFailureErrorCode:
    return cast(StreamFailureErrorCode, data)
