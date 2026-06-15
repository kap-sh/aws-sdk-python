"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Logs_20140328``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_cloudwatch_logs._auth._signers
import aws_sdk_cloudwatch_logs._auth._sigv4
from aws_sdk_cloudwatch_logs._auth._identity import Credentials
from aws_sdk_cloudwatch_logs._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_cloudwatch_logs._auth._zapros_handler import AuthMiddleware
from aws_sdk_cloudwatch_logs._pagination import resolve_path as _resolve_path
from aws_sdk_cloudwatch_logs._services._aws_config import aws_config
from aws_sdk_cloudwatch_logs._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.access_policy
    import aws_sdk_cloudwatch_logs.types.account_ids
    import aws_sdk_cloudwatch_logs.types.account_policy_document
    import aws_sdk_cloudwatch_logs.types.aggregate_log_group_summary
    import aws_sdk_cloudwatch_logs.types.amazon_resource_name
    import aws_sdk_cloudwatch_logs.types.anomaly
    import aws_sdk_cloudwatch_logs.types.anomaly_detector
    import aws_sdk_cloudwatch_logs.types.anomaly_detector_arn
    import aws_sdk_cloudwatch_logs.types.anomaly_id
    import aws_sdk_cloudwatch_logs.types.anomaly_visibility_t