"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AmazonDMSv20160101``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_database_migration_service._auth._signers
import aws_sdk_database_migration_service._auth._sigv4
from aws_sdk_database_migration_service._auth._identity import Credentials
from aws_sdk_database_migration_service._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_database_migration_service._auth._zapros_handler import AuthMiddleware
from aws_sdk_database_migration_service._pagination import resolve_path as _resolve_path
from aws_sdk_database_migration_service._services._aws_config import aws_config
from aws_sdk_database_migration_service._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.add_tags_to_resource_message
    import aws_sdk_database_migration_service.types.add_tags_to_resource_response
    import aws_sdk_database_migration_service.types.apply_pending_maintenance_action_message
    import aws_sdk_database_migration_service.types.apply_pending_maintenance_action_response
    import aws_sdk_database_migration_service.types.arn_list
    import aws_sdk_database_migration_service.types.assessment_report_types_list
    import aws_sdk_database_migration_service.types.batch_start_recommendations_request
    import aws_sdk_database_migration_service.types.batch_start_recommendations_response
    import aws_sdk_database_migration_service.types.boolean
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.cancel_metadata_model_conversion_message
    import aws_sdk_database_migration_service.types.cancel_metadata_model_conversion_response
    import aws_sdk_database_migration_service.types.cancel_metadata_model_creation_message
    import aws_sdk_database_migration_service.types.cancel_metadata_model_creation_response
    import aws_sdk_database_migration_service.types.cancel_replication_task_assessment_run_message
    import aws_sdk_database_migration_service.types.cancel_replication_task_assessment_run_response
    import aws_sdk_database_migration_service.types.certificate_walle