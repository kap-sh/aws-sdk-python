"""Generated from Smithy shape ``com.amazonaws.finspacedata#AWSHabaneroPublicAPI``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_finspace_data._auth._signers
import aws_sdk_finspace_data._auth._sigv4
from aws_sdk_finspace_data._auth._identity import Credentials
from aws_sdk_finspace_data._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_finspace_data._auth._zapros_handler import AuthMiddleware
from aws_sdk_finspace_data._pagination import resolve_path as _resolve_path
from aws_sdk_finspace_data._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.alias_string
    import aws_sdk_finspace_data.types.api_access
    import aws_sdk_finspace_data.types.application_permission_list
    import aws_sdk_finspace_data.types.associate_user_to_permission_group_request
    import aws_sdk_finspace_data.types.associate_user_to_permission_group_response
    import aws_sdk_finspace_data.types.boolean
    import aws_sdk_finspace_data.types.change_type
    import aws_sdk_finspace_data.types.changeset_id
    import aws_sdk_finspace_data.types.changeset_summary
    import aws_sdk_finspace_data.types.client_token
    import aws_sdk_finspace_data.types.create_changeset_request
    import aws_sdk_finspace_data.types.create_changeset_response
    import aws_sdk_finspace_data.types.create_data_view_request
    import aws_sdk_finspace_data.types.create_data_view_response
    import aws_sdk_finspace_data.types.create_dataset_request
    import aws_sdk_finspace_data.types.create_dataset_response
    import aws_sdk_finspace_data.types.create_permission_group_request
    import aws_sdk_finspace_data.types.create_permission_group_response
    import aws_sdk_finspace_data.types.create_user_request
    import aws_sdk_finspace_data.types.create_user_response
    import aws_sdk_finspace_data.types.data_view_destination_type_params
    import aws_sdk_finspace_data.types.data_view_id
    import aws_sdk_finspace_data.types.data_view_summary
    import aws_sdk_finspace_data.types.dataset
    import aws_sdk_finspace_data.types.dataset_description
    import aws_sdk_finspace_data.types.dataset_id
    import aws_sdk_finspace_data.types.dataset_kind
    import aws_sdk_finspace_data.types.dataset_owner_info
    import aws_sdk_finspace_data.types.dataset_title
    import aws_sdk_finspace_data.types.delete_dataset_request
    import aws_sdk_finspace_data.types.delete_dataset_response
    import aws_sdk_finspace_data.types.delete_permission_group_request
    import aws_sdk_finspace_data.types.delete_permission_group_response
    import aws_sdk_finspace_data.types.disable_user_request
    import aws_sdk_finspace_data.types.disable_user_response
    import aws_sdk_finspace_data.types.disassociate_user_from_permission_group_request
    import aws_sdk_finspace_data.types.disassociate_user_from_permission_group_response
    import aws_sdk_finspace_data.types.email
    import aws_sdk_finspace_data.types.enable_user_request
    import aws_sdk_finspace_data.types.enable_user_response
    import aws_sdk_finspace_data.types.first_name
    import aws_sdk_finspace_data.types.format_params
    import aws_sdk_finspace_data.types.get_changeset_request
    import aws_sdk_finspace_data.types.get_changeset_response
    import aws_sdk_finspace_data.types.get_data_view_request
    import aws_sdk_finspace_data.types.get_data_view_response
    import aws_sdk_finspace_data.types.get_dataset_request
    import aws_sdk_finspace_data.types.get_dataset_response
    import aws_sdk_finspace_data.types.get_external_data_view_access_details_request
    import aws_sdk_finspace_data.types.get_external_data_view_access_details_response
    import aws_sdk_finspace_data.types.get_permission_group_request
    import aws_sdk_finspace_data.types.get_permission_group_response
    import aws_sdk_finspace_data.types.get_programmatic_access_credentials_request
    import aws_sdk_finspace_data.types.get_programmatic_access_credentials_response
    import aws_sdk_finspace_data.types.get_user_request
    import aws_sdk_finspace_data.types.get_user_response
    import aws_sdk_finspace_data.types.get_working_location_request
    import aws_sdk_finspace_data.types.get_working_location_response
    import aws_sdk_finspace_data.types.id_type
    import aws_sdk_finspace_data.types.last_name
    import aws_sdk_finspace_data.types.list_changesets_request
    import aws_sdk_finspace_data.types.list_changesets_response
    import aws_sdk_finspace_data.types.list_data_views_request
    import aws_sdk_finspace_data.types.list_data_views_response
    import aws_sdk_finspace_data.types.list_datasets_request
    import aws_sdk_finspace_data.types.list_datasets_response
    import aws_sdk_finspace_data.types.list_permission_groups_by_user_request
    import aws_sdk_finspace_data.types.list_permission_groups_by_user_response
    import aws_sdk_finspace_data.types.list_permission_groups_request
    import aws_sdk_finspace_data.types.list_permission_groups_response
    import aws_sdk_finspace_data.types.list_users_by_permission_group_request
    import aws_sdk_finspace_data.types.list_users_by_permission_group_response
    import aws_sdk_finspace_data.types.list_users_request
    import aws_sdk_finspace_data.types.list_users_response
    import aws_sdk_finspace_data.types.location_type
    import aws_sdk_finspace_data.types.pagination_token
    import aws_sdk_finspace_data.types.partition_column_list
    import aws_sdk_finspace_data.types.permission_group
    import aws_sdk_finspace_data.types.permission_group_description
    import aws_sdk_finspace_data.types.permission_group_id
    import aws_sdk_finspace_data.types.permission_group_name
    import aws_sdk_finspace_data.types.permission_group_params
    import aws_sdk_finspace_data.types.reset_user_password_request
    import aws_sdk_finspace_data.types.reset_user_password_response
    import aws_sdk_finspace_data.types.result_limit
    import aws_sdk_finspace_data.types.role_arn
    import aws_sdk_finspace_data.types.schema_union
    import aws_sdk_finspace_data.types.session_duration
    import aws_sdk_finspace_data.types.sort_column_list
    import aws_sdk_finspace_data.types.source_params
    import aws_sdk_finspace_data.types.string_value_length1to255
    import aws_sdk_finspace_data.types.timestamp_epoch
    import aws_sdk_finspace_data.types.update_changeset_request
    import aws_sdk_finspace_data.types.update_changeset_response
    import aws_sdk_finspace_data.types.update_dataset_request
    import aws_sdk_finspace_data.types.update_dataset_response
    import aws_sdk_finspace_data.types.update_permission_group_request
    import aws_sdk_finspace_data.types.update_permission_group_response
    import aws_sdk_finspace_data.types.update_user_request
    import aws_sdk_finspace_data.types.update_user_response
    import aws_sdk_finspace_data.types.user
    import aws_sdk_finspace_data.types.user_id
    import aws_sdk_finspace_data.types.user_type


class AsyncfinspacedataClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncfinspacedataClient:
    """A client for the ``finspacedata`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = AsyncfinspacedataClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncfinspacedataClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncfinspacedataClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def associate_user_to_permission_group(
        self,
        permission_group_id: "aws_sdk_finspace_data.types.permission_group_id.PermissionGroupId",
        user_id: "aws_sdk_finspace_data.types.user_id.UserId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.associate_user_to_permission_group_response.AssociateUserToPermissionGroupResponse":
        """<p>Adds a user to a permission group to grant permissions for actions a user can perform in FinSpace.</p>

        Args:
            permission_group_id: <p>The unique identifier for the permission group.</p>
            user_id: <p>The unique identifier for the user.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.associate_user_to_permission_group_request.AssociateUserToPermissionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.associate_user_to_permission_group_response.AssociateUserToPermissionGroupResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.associate_user_to_permission_group

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.associate_user_to_permission_group.async_associate_user_to_permission_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.associate_user_to_permission_group_request.AssociateUserToPermissionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["permission_group_id"] = permission_group_id
        input_["user_id"] = user_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_changeset(
        self,
        dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId",
        change_type: "aws_sdk_finspace_data.types.change_type.ChangeType",
        source_params: "aws_sdk_finspace_data.types.source_params.SourceParams",
        format_params: "aws_sdk_finspace_data.types.format_params.FormatParams",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "aws_sdk_finspace_data.types.create_changeset_response.CreateChangesetResponse"
    ):
        r"""<p>Creates a new Changeset in a FinSpace Dataset.</p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            dataset_id: <p>The unique identifier for the FinSpace Dataset where the Changeset will be created. </p>
            change_type: <p>The option to indicate how a Changeset will be applied to a Dataset.</p> <ul> <li> <p> <code>REPLACE</code> – Changeset will be considered as a replacement to all prior loaded Changesets.</p> </li> <li> <p> <code>APPEND</code> – Changeset will be considered as an addition to the end of all prior loaded Changesets.</p> </li> <li> <p> <code>MODIFY</code> – Changeset is considered as a replacement to a specific prior ingested Changeset.</p> </li> </ul>
            source_params: <p>Options that define the location of the data being ingested (<code>s3SourcePath</code>) and the source of the changeset (<code>sourceType</code>).</p> <p>Both <code>s3SourcePath</code> and <code>sourceType</code> are required attributes.</p> <p>Here is an example of how you could specify the <code>sourceParams</code>:</p> <p> <code> \"sourceParams\": { \"s3SourcePath\": \"s3://finspace-landing-us-east-2-bk7gcfvitndqa6ebnvys4d/scratch/wr5hh8pwkpqqkxa4sxrmcw/ingestion/equity.csv\", \"sourceType\": \"S3\" } </code> </p> <p>The S3 path that you specify must allow the FinSpace role access. To do that, you first need to configure the IAM policy on S3 bucket. For more information, see <a href=\"https://docs.aws.amazon.com/finspace/latest/data-api/fs-using-the-finspace-api.html#access-s3-buckets\">Loading data from an Amazon S3 Bucket using the FinSpace API</a> section.</p>
            format_params: <p>Options that define the structure of the source file(s) including the format type (<code>formatType</code>), header row (<code>withHeader</code>), data separation character (<code>separator</code>) and the type of compression (<code>compression</code>). </p> <p> <code>formatType</code> is a required attribute and can have the following values: </p> <ul> <li> <p> <code>PARQUET</code> – Parquet source file format.</p> </li> <li> <p> <code>CSV</code> – CSV source file format.</p> </li> <li> <p> <code>JSON</code> – JSON source file format.</p> </li> <li> <p> <code>XML</code> – XML source file format.</p> </li> </ul> <p>Here is an example of how you could specify the <code>formatParams</code>:</p> <p> <code> \"formatParams\": { \"formatType\": \"CSV\", \"withHeader\": \"true\", \"separator\": \",\", \"compression\":\"None\" } </code> </p> <p>Note that if you only provide <code>formatType</code> as <code>CSV</code>, the rest of the attributes will automatically default to CSV values as following:</p> <p> <code> { \"withHeader\": \"true\", \"separator\": \",\" } </code> </p> <p> For more information about supported file formats, see <a href=\"https://docs.aws.amazon.com/finspace/latest/userguide/supported-data-types.html\">Supported Data Types and File Formats</a> in the FinSpace User Guide.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.create_changeset_request.CreateChangesetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.create_changeset_response.CreateChangesetResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.create_changeset

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.create_changeset.async_create_changeset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.create_changeset_request.CreateChangesetRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["dataset_id"] = dataset_id
        input_["change_type"] = change_type
        input_["source_params"] = source_params
        input_["format_params"] = format_params

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_dataset(
        self,
        dataset_title: "aws_sdk_finspace_data.types.dataset_title.DatasetTitle",
        kind: "aws_sdk_finspace_data.types.dataset_kind.DatasetKind",
        permission_group_params: "aws_sdk_finspace_data.types.permission_group_params.PermissionGroupParams",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
        dataset_description: Optional[
            "aws_sdk_finspace_data.types.dataset_description.DatasetDescription"
        ] = None,
        owner_info: Optional[
            "aws_sdk_finspace_data.types.dataset_owner_info.DatasetOwnerInfo"
        ] = None,
        alias: Optional["aws_sdk_finspace_data.types.alias_string.AliasString"] = None,
        schema_definition: Optional[
            "aws_sdk_finspace_data.types.schema_union.SchemaUnion"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.create_dataset_response.CreateDatasetResponse":
        """<p>Creates a new FinSpace Dataset.</p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            dataset_title: <p>Display title for a FinSpace Dataset.</p>
            kind: <p>The format in which Dataset data is structured.</p> <ul> <li> <p> <code>TABULAR</code> – Data is structured in a tabular format.</p> </li> <li> <p> <code>NON_TABULAR</code> – Data is structured in a non-tabular format.</p> </li> </ul>
            dataset_description: <p>Description of a Dataset.</p>
            owner_info: <p>Contact information for a Dataset owner.</p>
            permission_group_params: <p>Permission group parameters for Dataset permissions.</p>
            alias: <p>The unique resource identifier for a Dataset.</p>
            schema_definition: <p>Definition for a schema on a tabular Dataset.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.create_dataset_request.CreateDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.create_dataset_response.CreateDatasetResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.create_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.create_dataset.async_create_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.create_dataset_request.CreateDatasetRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["dataset_title"] = dataset_title
        input_["kind"] = kind
        if dataset_description is not None:
            input_["dataset_description"] = dataset_description
        if owner_info is not None:
            input_["owner_info"] = owner_info
        input_["permission_group_params"] = permission_group_params
        if alias is not None:
            input_["alias"] = alias
        if schema_definition is not None:
            input_["schema_definition"] = schema_definition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_data_view(
        self,
        dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId",
        destination_type_params: "aws_sdk_finspace_data.types.data_view_destination_type_params.DataViewDestinationTypeParams",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
        auto_update: Optional["aws_sdk_finspace_data.types.boolean.Boolean"] = None,
        sort_columns: Optional[
            "aws_sdk_finspace_data.types.sort_column_list.SortColumnList"
        ] = None,
        partition_columns: Optional[
            "aws_sdk_finspace_data.types.partition_column_list.PartitionColumnList"
        ] = None,
        as_of_timestamp: Optional[
            "aws_sdk_finspace_data.types.timestamp_epoch.TimestampEpoch"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.create_data_view_response.CreateDataViewResponse":
        """<p>Creates a Dataview for a Dataset.</p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            dataset_id: <p>The unique Dataset identifier that is used to create a Dataview.</p>
            auto_update: <p>Flag to indicate Dataview should be updated automatically.</p>
            sort_columns: <p>Columns to be used for sorting the data.</p>
            partition_columns: <p>Ordered set of column names used to partition data.</p>
            as_of_timestamp: <p>Beginning time to use for the Dataview. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>
            destination_type_params: <p>Options that define the destination type for the Dataview.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.create_data_view_request.CreateDataViewRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.create_data_view_response.CreateDataViewResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.create_data_view

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.create_data_view.async_create_data_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.create_data_view_request.CreateDataViewRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["dataset_id"] = dataset_id
        if auto_update is not None:
            input_["auto_update"] = auto_update
        if sort_columns is not None:
            input_["sort_columns"] = sort_columns
        if partition_columns is not None:
            input_["partition_columns"] = partition_columns
        if as_of_timestamp is not None:
            input_["as_of_timestamp"] = as_of_timestamp
        input_["destination_type_params"] = destination_type_params

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_permission_group(
        self,
        name: "aws_sdk_finspace_data.types.permission_group_name.PermissionGroupName",
        application_permissions: "aws_sdk_finspace_data.types.application_permission_list.ApplicationPermissionList",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        description: Optional[
            "aws_sdk_finspace_data.types.permission_group_description.PermissionGroupDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.create_permission_group_response.CreatePermissionGroupResponse":
        """<p>Creates a group of permissions for various actions that a user can perform in FinSpace.</p>

        Args:
            name: <p>The name of the permission group.</p>
            description: <p>A brief description for the permission group.</p>
            application_permissions: <p>The option to indicate FinSpace application permissions that are granted to a specific group.</p> <important> <p>When assigning application permissions, be aware that the permission <code>ManageUsersAndGroups</code> allows users to grant themselves or others access to any functionality in their FinSpace environment's application. It should only be granted to trusted users.</p> </important> <ul> <li> <p> <code>CreateDataset</code> – Group members can create new datasets.</p> </li> <li> <p> <code>ManageClusters</code> – Group members can manage Apache Spark clusters from FinSpace notebooks.</p> </li> <li> <p> <code>ManageUsersAndGroups</code> – Group members can manage users and permission groups. This is a privileged permission that allows users to grant themselves or others access to any functionality in the application. It should only be granted to trusted users.</p> </li> <li> <p> <code>ManageAttributeSets</code> – Group members can manage attribute sets.</p> </li> <li> <p> <code>ViewAuditData</code> – Group members can view audit data.</p> </li> <li> <p> <code>AccessNotebooks</code> – Group members will have access to FinSpace notebooks.</p> </li> <li> <p> <code>GetTemporaryCredentials</code> – Group members can get temporary API credentials.</p> </li> </ul>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.create_permission_group_request.CreatePermissionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.create_permission_group_response.CreatePermissionGroupResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.create_permission_group

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.create_permission_group.async_create_permission_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.create_permission_group_request.CreatePermissionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["application_permissions"] = application_permissions
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_user(
        self,
        email_address: "aws_sdk_finspace_data.types.email.Email",
        type: "aws_sdk_finspace_data.types.user_type.UserType",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        first_name: Optional["aws_sdk_finspace_data.types.first_name.FirstName"] = None,
        last_name: Optional["aws_sdk_finspace_data.types.last_name.LastName"] = None,
        api_access: Optional["aws_sdk_finspace_data.types.api_access.ApiAccess"] = None,
        api_access_principal_arn: Optional[
            "aws_sdk_finspace_data.types.role_arn.RoleArn"
        ] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.create_user_response.CreateUserResponse":
        """<p>Creates a new user in FinSpace.</p>

        Args:
            email_address: <p>The email address of the user that you want to register. The email address serves as a uniquer identifier for each user and cannot be changed after it's created.</p>
            type: <p>The option to indicate the type of user. Use one of the following options to specify this parameter:</p> <ul> <li> <p> <code>SUPER_USER</code> – A user with permission to all the functionality and data in FinSpace.</p> </li> <li> <p> <code>APP_USER</code> – A user with specific permissions in FinSpace. The users are assigned permissions by adding them to a permission group.</p> </li> </ul>
            first_name: <p>The first name of the user that you want to register.</p>
            last_name: <p>The last name of the user that you want to register.</p>
            api_access: <p>The option to indicate whether the user can use the <code>GetProgrammaticAccessCredentials</code> API to obtain credentials that can then be used to access other FinSpace Data API operations.</p> <ul> <li> <p> <code>ENABLED</code> – The user has permissions to use the APIs.</p> </li> <li> <p> <code>DISABLED</code> – The user does not have permissions to use any APIs.</p> </li> </ul>
            api_access_principal_arn: <p>The ARN identifier of an AWS user or role that is allowed to call the <code>GetProgrammaticAccessCredentials</code> API to obtain a credentials token for a specific FinSpace user. This must be an IAM role within your FinSpace account.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.create_user_request.CreateUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.create_user_response.CreateUserResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.create_user

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.create_user.async_create_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.create_user_request.CreateUserRequest = {}  # type: ignore[typeddict-item]
        input_["email_address"] = email_address
        input_["type"] = type
        if first_name is not None:
            input_["first_name"] = first_name
        if last_name is not None:
            input_["last_name"] = last_name
        if api_access is not None:
            input_["api_access"] = api_access
        if api_access_principal_arn is not None:
            input_["api_access_principal_arn"] = api_access_principal_arn
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_dataset(
        self,
        dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.delete_dataset_response.DeleteDatasetResponse":
        """<p>Deletes a FinSpace Dataset.</p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            dataset_id: <p>The unique identifier of the Dataset to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.delete_dataset_request.DeleteDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.delete_dataset_response.DeleteDatasetResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.delete_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.delete_dataset.async_delete_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.delete_dataset_request.DeleteDatasetRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["dataset_id"] = dataset_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_permission_group(
        self,
        permission_group_id: "aws_sdk_finspace_data.types.permission_group_id.PermissionGroupId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.delete_permission_group_response.DeletePermissionGroupResponse":
        """<p>Deletes a permission group. This action is irreversible.</p>

        Args:
            permission_group_id: <p>The unique identifier for the permission group that you want to delete.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.delete_permission_group_request.DeletePermissionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.delete_permission_group_response.DeletePermissionGroupResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.delete_permission_group

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.delete_permission_group.async_delete_permission_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.delete_permission_group_request.DeletePermissionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["permission_group_id"] = permission_group_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disable_user(
        self,
        user_id: "aws_sdk_finspace_data.types.user_id.UserId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.disable_user_response.DisableUserResponse":
        """<p>Denies access to the FinSpace web application and API for the specified user.</p>

        Args:
            user_id: <p>The unique identifier for the user that you want to deactivate.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.disable_user_request.DisableUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.disable_user_response.DisableUserResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.disable_user

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.disable_user.async_disable_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.disable_user_request.DisableUserRequest = {}  # type: ignore[typeddict-item]
        input_["user_id"] = user_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_user_from_permission_group(
        self,
        permission_group_id: "aws_sdk_finspace_data.types.permission_group_id.PermissionGroupId",
        user_id: "aws_sdk_finspace_data.types.user_id.UserId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.disassociate_user_from_permission_group_response.DisassociateUserFromPermissionGroupResponse":
        """<p>Removes a user from a permission group.</p>

        Args:
            permission_group_id: <p>The unique identifier for the permission group.</p>
            user_id: <p>The unique identifier for the user.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.disassociate_user_from_permission_group_request.DisassociateUserFromPermissionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.disassociate_user_from_permission_group_response.DisassociateUserFromPermissionGroupResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.disassociate_user_from_permission_group

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.disassociate_user_from_permission_group.async_disassociate_user_from_permission_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.disassociate_user_from_permission_group_request.DisassociateUserFromPermissionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["permission_group_id"] = permission_group_id
        input_["user_id"] = user_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def enable_user(
        self,
        user_id: "aws_sdk_finspace_data.types.user_id.UserId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.enable_user_response.EnableUserResponse":
        """<p> Allows the specified user to access the FinSpace web application and API.</p>

        Args:
            user_id: <p>The unique identifier for the user that you want to activate.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.enable_user_request.EnableUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.enable_user_response.EnableUserResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.enable_user

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.enable_user.async_enable_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.enable_user_request.EnableUserRequest = {}  # type: ignore[typeddict-item]
        input_["user_id"] = user_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_changeset(
        self,
        dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId",
        changeset_id: "aws_sdk_finspace_data.types.changeset_id.ChangesetId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
    ) -> "aws_sdk_finspace_data.types.get_changeset_response.GetChangesetResponse":
        """<p>Get information about a Changeset.</p>

        Args:
            dataset_id: <p>The unique identifier for the FinSpace Dataset where the Changeset is created.</p>
            changeset_id: <p>The unique identifier of the Changeset for which to get data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.get_changeset_request.GetChangesetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.get_changeset_response.GetChangesetResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.get_changeset

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.get_changeset.async_get_changeset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.get_changeset_request.GetChangesetRequest = {}  # type: ignore[typeddict-item]
        input_["dataset_id"] = dataset_id
        input_["changeset_id"] = changeset_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_dataset(
        self,
        dataset_id: "aws_sdk_finspace_data.types.string_value_length1to255.StringValueLength1to255",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
    ) -> "aws_sdk_finspace_data.types.get_dataset_response.GetDatasetResponse":
        """<p>Returns information about a Dataset.</p>

        Args:
            dataset_id: <p>The unique identifier for a Dataset.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.get_dataset_request.GetDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.get_dataset_response.GetDatasetResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.get_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.get_dataset.async_get_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.get_dataset_request.GetDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["dataset_id"] = dataset_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_data_view(
        self,
        data_view_id: "aws_sdk_finspace_data.types.data_view_id.DataViewId",
        dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
    ) -> "aws_sdk_finspace_data.types.get_data_view_response.GetDataViewResponse":
        """<p>Gets information about a Dataview.</p>

        Args:
            data_view_id: <p>The unique identifier for the Dataview.</p>
            dataset_id: <p>The unique identifier for the Dataset used in the Dataview.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.get_data_view_request.GetDataViewRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.get_data_view_response.GetDataViewResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.get_data_view

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.get_data_view.async_get_data_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.get_data_view_request.GetDataViewRequest = {}  # type: ignore[typeddict-item]
        input_["data_view_id"] = data_view_id
        input_["dataset_id"] = dataset_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_external_data_view_access_details(
        self,
        data_view_id: "aws_sdk_finspace_data.types.data_view_id.DataViewId",
        dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
    ) -> "aws_sdk_finspace_data.types.get_external_data_view_access_details_response.GetExternalDataViewAccessDetailsResponse":
        """<p>Returns the credentials to access the external Dataview from an S3 location. To call this API:</p> <ul> <li> <p>You must retrieve the programmatic credentials.</p> </li> <li> <p>You must be a member of a FinSpace user group, where the dataset that you want to access has <code>Read Dataset Data</code> permissions.</p> </li> </ul>

        Args:
            data_view_id: <p>The unique identifier for the Dataview that you want to access.</p>
            dataset_id: <p>The unique identifier for the Dataset.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.get_external_data_view_access_details_request.GetExternalDataViewAccessDetailsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.get_external_data_view_access_details_response.GetExternalDataViewAccessDetailsResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.get_external_data_view_access_details

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.get_external_data_view_access_details.async_get_external_data_view_access_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.get_external_data_view_access_details_request.GetExternalDataViewAccessDetailsRequest = {}  # type: ignore[typeddict-item]
        input_["data_view_id"] = data_view_id
        input_["dataset_id"] = dataset_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_permission_group(
        self,
        permission_group_id: "aws_sdk_finspace_data.types.permission_group_id.PermissionGroupId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
    ) -> "aws_sdk_finspace_data.types.get_permission_group_response.GetPermissionGroupResponse":
        """<p>Retrieves the details of a specific permission group.</p>

        Args:
            permission_group_id: <p>The unique identifier for the permission group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.get_permission_group_request.GetPermissionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.get_permission_group_response.GetPermissionGroupResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.get_permission_group

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.get_permission_group.async_get_permission_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.get_permission_group_request.GetPermissionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["permission_group_id"] = permission_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_programmatic_access_credentials(
        self,
        environment_id: "aws_sdk_finspace_data.types.id_type.IdType",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        duration_in_minutes: Optional[
            "aws_sdk_finspace_data.types.session_duration.SessionDuration"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.get_programmatic_access_credentials_response.GetProgrammaticAccessCredentialsResponse":
        r"""<p>Request programmatic credentials to use with FinSpace SDK. For more information, see <a href=\"https://docs.aws.amazon.com/finspace/latest/data-api/fs-using-the-finspace-api.html#accessing-credentials\">Step 2. Access credentials programmatically using IAM access key id and secret access key</a>.</p>

        Args:
            duration_in_minutes: <p>The time duration in which the credentials remain valid. </p>
            environment_id: <p>The FinSpace environment identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.get_programmatic_access_credentials_request.GetProgrammaticAccessCredentialsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.get_programmatic_access_credentials_response.GetProgrammaticAccessCredentialsResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.get_programmatic_access_credentials

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.get_programmatic_access_credentials.async_get_programmatic_access_credentials(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.get_programmatic_access_credentials_request.GetProgrammaticAccessCredentialsRequest = {}  # type: ignore[typeddict-item]
        if duration_in_minutes is not None:
            input_["duration_in_minutes"] = duration_in_minutes
        input_["environment_id"] = environment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_user(
        self,
        user_id: "aws_sdk_finspace_data.types.user_id.UserId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
    ) -> "aws_sdk_finspace_data.types.get_user_response.GetUserResponse":
        """<p>Retrieves details for a specific user.</p>

        Args:
            user_id: <p>The unique identifier of the user to get data for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.get_user_request.GetUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.get_user_response.GetUserResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.get_user

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.get_user.async_get_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.get_user_request.GetUserRequest = {}  # type: ignore[typeddict-item]
        input_["user_id"] = user_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_working_location(
        self,
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        location_type: Optional[
            "aws_sdk_finspace_data.types.location_type.locationType"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.get_working_location_response.GetWorkingLocationResponse":
        """<p>A temporary Amazon S3 location, where you can copy your files from a source location to stage or use as a scratch space in FinSpace notebook.</p>

        Args:
            location_type: <p>Specify the type of the working location.</p> <ul> <li> <p> <code>SAGEMAKER</code> – Use the Amazon S3 location as a temporary location to store data content when working with FinSpace Notebooks that run on SageMaker studio.</p> </li> <li> <p> <code>INGESTION</code> – Use the Amazon S3 location as a staging location to copy your data content and then use the location with the Changeset creation operation.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.get_working_location_request.GetWorkingLocationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.get_working_location_response.GetWorkingLocationResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.get_working_location

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.get_working_location.async_get_working_location(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.get_working_location_request.GetWorkingLocationRequest = {}  # type: ignore[typeddict-item]
        if location_type is not None:
            input_["location_type"] = location_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_changesets(
        self,
        dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        max_results: Optional[
            "aws_sdk_finspace_data.types.result_limit.ResultLimit"
        ] = None,
        next_token: Optional[
            "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.list_changesets_response.ListChangesetsResponse":
        """<p>Lists the FinSpace Changesets for a Dataset.</p>

        Args:
            dataset_id: <p>The unique identifier for the FinSpace Dataset to which the Changeset belongs.</p>
            max_results: <p>The maximum number of results per page.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.list_changesets_request.ListChangesetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.list_changesets_response.ListChangesetsResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.list_changesets

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.list_changesets.async_list_changesets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.list_changesets_request.ListChangesetsRequest = {}  # type: ignore[typeddict-item]
        input_["dataset_id"] = dataset_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_changesets(
        self,
        dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        max_results: Optional[
            "aws_sdk_finspace_data.types.result_limit.ResultLimit"
        ] = None,
        next_token: Optional[
            "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "AsyncIterator[aws_sdk_finspace_data.types.changeset_summary.ChangesetSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_changesets(
                dataset_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("changesets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_datasets(
        self,
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_finspace_data.types.result_limit.ResultLimit"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.list_datasets_response.ListDatasetsResponse":
        """<p>Lists all of the active Datasets that a user has access to.</p>

        Args:
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.list_datasets_request.ListDatasetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.list_datasets_response.ListDatasetsResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.list_datasets

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.list_datasets.async_list_datasets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.list_datasets_request.ListDatasetsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_datasets(
        self,
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_finspace_data.types.result_limit.ResultLimit"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_finspace_data.types.dataset.Dataset]":
        _token = next_token
        while True:
            _response = await self.list_datasets(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("datasets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_views(
        self,
        dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_finspace_data.types.result_limit.ResultLimit"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.list_data_views_response.ListDataViewsResponse":
        """<p>Lists all available Dataviews for a Dataset.</p>

        Args:
            dataset_id: <p>The unique identifier of the Dataset for which to retrieve Dataviews.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.list_data_views_request.ListDataViewsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.list_data_views_response.ListDataViewsResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.list_data_views

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.list_data_views.async_list_data_views(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.list_data_views_request.ListDataViewsRequest = {}  # type: ignore[typeddict-item]
        input_["dataset_id"] = dataset_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_data_views(
        self,
        dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_finspace_data.types.result_limit.ResultLimit"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_finspace_data.types.data_view_summary.DataViewSummary]":
        _token = next_token
        while True:
            _response = await self.list_data_views(
                dataset_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_views",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_permission_groups(
        self,
        max_results: "aws_sdk_finspace_data.types.result_limit.ResultLimit",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.list_permission_groups_response.ListPermissionGroupsResponse":
        """<p>Lists all available permission groups in FinSpace.</p>

        Args:
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.list_permission_groups_request.ListPermissionGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.list_permission_groups_response.ListPermissionGroupsResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.list_permission_groups

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.list_permission_groups.async_list_permission_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.list_permission_groups_request.ListPermissionGroupsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_permission_groups(
        self,
        max_results: "aws_sdk_finspace_data.types.result_limit.ResultLimit",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_finspace_data.types.permission_group.PermissionGroup]":
        _token = next_token
        while True:
            _response = await self.list_permission_groups(
                max_results,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("permission_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_permission_groups_by_user(
        self,
        user_id: "aws_sdk_finspace_data.types.user_id.UserId",
        max_results: "aws_sdk_finspace_data.types.result_limit.ResultLimit",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.list_permission_groups_by_user_response.ListPermissionGroupsByUserResponse":
        """<p>Lists all the permission groups that are associated with a specific user.</p>

        Args:
            user_id: <p>The unique identifier for the user.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.list_permission_groups_by_user_request.ListPermissionGroupsByUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.list_permission_groups_by_user_response.ListPermissionGroupsByUserResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.list_permission_groups_by_user

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.list_permission_groups_by_user.async_list_permission_groups_by_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.list_permission_groups_by_user_request.ListPermissionGroupsByUserRequest = {}  # type: ignore[typeddict-item]
        input_["user_id"] = user_id
        if next_token is not None:
            input_["next_token"] = next_token
        input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_users(
        self,
        max_results: "aws_sdk_finspace_data.types.result_limit.ResultLimit",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.list_users_response.ListUsersResponse":
        """<p>Lists all available users in FinSpace.</p>

        Args:
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.list_users_request.ListUsersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.list_users_response.ListUsersResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.list_users

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.list_users.async_list_users(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.list_users_request.ListUsersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_users(
        self,
        max_results: "aws_sdk_finspace_data.types.result_limit.ResultLimit",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_finspace_data.types.user.User]":
        _token = next_token
        while True:
            _response = await self.list_users(
                max_results,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("users",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_users_by_permission_group(
        self,
        permission_group_id: "aws_sdk_finspace_data.types.permission_group_id.PermissionGroupId",
        max_results: "aws_sdk_finspace_data.types.result_limit.ResultLimit",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.list_users_by_permission_group_response.ListUsersByPermissionGroupResponse":
        """<p>Lists details of all the users in a specific permission group.</p>

        Args:
            permission_group_id: <p>The unique identifier for the permission group.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.list_users_by_permission_group_request.ListUsersByPermissionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.list_users_by_permission_group_response.ListUsersByPermissionGroupResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.list_users_by_permission_group

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.list_users_by_permission_group.async_list_users_by_permission_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.list_users_by_permission_group_request.ListUsersByPermissionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["permission_group_id"] = permission_group_id
        if next_token is not None:
            input_["next_token"] = next_token
        input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reset_user_password(
        self,
        user_id: "aws_sdk_finspace_data.types.user_id.UserId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.reset_user_password_response.ResetUserPasswordResponse":
        """<p>Resets the password for a specified user ID and generates a temporary one. Only a superuser can reset password for other users. Resetting the password immediately invalidates the previous password associated with the user.</p>

        Args:
            user_id: <p>The unique identifier of the user that a temporary password is requested for.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.reset_user_password_request.ResetUserPasswordRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.reset_user_password_response.ResetUserPasswordResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.reset_user_password

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.reset_user_password.async_reset_user_password(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.reset_user_password_request.ResetUserPasswordRequest = {}  # type: ignore[typeddict-item]
        input_["user_id"] = user_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_changeset(
        self,
        dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId",
        changeset_id: "aws_sdk_finspace_data.types.changeset_id.ChangesetId",
        source_params: "aws_sdk_finspace_data.types.source_params.SourceParams",
        format_params: "aws_sdk_finspace_data.types.format_params.FormatParams",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "aws_sdk_finspace_data.types.update_changeset_response.UpdateChangesetResponse"
    ):
        r"""<p>Updates a FinSpace Changeset.</p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            dataset_id: <p>The unique identifier for the FinSpace Dataset in which the Changeset is created.</p>
            changeset_id: <p>The unique identifier for the Changeset to update.</p>
            source_params: <p>Options that define the location of the data being ingested (<code>s3SourcePath</code>) and the source of the changeset (<code>sourceType</code>).</p> <p>Both <code>s3SourcePath</code> and <code>sourceType</code> are required attributes.</p> <p>Here is an example of how you could specify the <code>sourceParams</code>:</p> <p> <code> \"sourceParams\": { \"s3SourcePath\": \"s3://finspace-landing-us-east-2-bk7gcfvitndqa6ebnvys4d/scratch/wr5hh8pwkpqqkxa4sxrmcw/ingestion/equity.csv\", \"sourceType\": \"S3\" } </code> </p> <p>The S3 path that you specify must allow the FinSpace role access. To do that, you first need to configure the IAM policy on S3 bucket. For more information, see <a href=\"https://docs.aws.amazon.com/finspace/latest/data-api/fs-using-the-finspace-api.html#access-s3-buckets\">Loading data from an Amazon S3 Bucket using the FinSpace API</a>section.</p>
            format_params: <p>Options that define the structure of the source file(s) including the format type (<code>formatType</code>), header row (<code>withHeader</code>), data separation character (<code>separator</code>) and the type of compression (<code>compression</code>). </p> <p> <code>formatType</code> is a required attribute and can have the following values: </p> <ul> <li> <p> <code>PARQUET</code> – Parquet source file format.</p> </li> <li> <p> <code>CSV</code> – CSV source file format.</p> </li> <li> <p> <code>JSON</code> – JSON source file format.</p> </li> <li> <p> <code>XML</code> – XML source file format.</p> </li> </ul> <p>Here is an example of how you could specify the <code>formatParams</code>:</p> <p> <code> \"formatParams\": { \"formatType\": \"CSV\", \"withHeader\": \"true\", \"separator\": \",\", \"compression\":\"None\" } </code> </p> <p>Note that if you only provide <code>formatType</code> as <code>CSV</code>, the rest of the attributes will automatically default to CSV values as following:</p> <p> <code> { \"withHeader\": \"true\", \"separator\": \",\" } </code> </p> <p> For more information about supported file formats, see <a href=\"https://docs.aws.amazon.com/finspace/latest/userguide/supported-data-types.html\">Supported Data Types and File Formats</a> in the FinSpace User Guide.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.update_changeset_request.UpdateChangesetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.update_changeset_response.UpdateChangesetResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.update_changeset

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.update_changeset.async_update_changeset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.update_changeset_request.UpdateChangesetRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["dataset_id"] = dataset_id
        input_["changeset_id"] = changeset_id
        input_["source_params"] = source_params
        input_["format_params"] = format_params

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_dataset(
        self,
        dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId",
        dataset_title: "aws_sdk_finspace_data.types.dataset_title.DatasetTitle",
        kind: "aws_sdk_finspace_data.types.dataset_kind.DatasetKind",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
        dataset_description: Optional[
            "aws_sdk_finspace_data.types.dataset_description.DatasetDescription"
        ] = None,
        alias: Optional["aws_sdk_finspace_data.types.alias_string.AliasString"] = None,
        schema_definition: Optional[
            "aws_sdk_finspace_data.types.schema_union.SchemaUnion"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.update_dataset_response.UpdateDatasetResponse":
        """<p>Updates a FinSpace Dataset.</p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            dataset_id: <p>The unique identifier for the Dataset to update.</p>
            dataset_title: <p>A display title for the Dataset.</p>
            kind: <p>The format in which the Dataset data is structured.</p> <ul> <li> <p> <code>TABULAR</code> – Data is structured in a tabular format.</p> </li> <li> <p> <code>NON_TABULAR</code> – Data is structured in a non-tabular format.</p> </li> </ul>
            dataset_description: <p>A description for the Dataset.</p>
            alias: <p>The unique resource identifier for a Dataset.</p>
            schema_definition: <p>Definition for a schema on a tabular Dataset.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.update_dataset_request.UpdateDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.update_dataset_response.UpdateDatasetResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.update_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.update_dataset.async_update_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.update_dataset_request.UpdateDatasetRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["dataset_id"] = dataset_id
        input_["dataset_title"] = dataset_title
        input_["kind"] = kind
        if dataset_description is not None:
            input_["dataset_description"] = dataset_description
        if alias is not None:
            input_["alias"] = alias
        if schema_definition is not None:
            input_["schema_definition"] = schema_definition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_permission_group(
        self,
        permission_group_id: "aws_sdk_finspace_data.types.permission_group_id.PermissionGroupId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        name: Optional[
            "aws_sdk_finspace_data.types.permission_group_name.PermissionGroupName"
        ] = None,
        description: Optional[
            "aws_sdk_finspace_data.types.permission_group_description.PermissionGroupDescription"
        ] = None,
        application_permissions: Optional[
            "aws_sdk_finspace_data.types.application_permission_list.ApplicationPermissionList"
        ] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.update_permission_group_response.UpdatePermissionGroupResponse":
        """<p>Modifies the details of a permission group. You cannot modify a <code>permissionGroupID</code>.</p>

        Args:
            permission_group_id: <p>The unique identifier for the permission group to update.</p>
            name: <p>The name of the permission group.</p>
            description: <p>A brief description for the permission group.</p>
            application_permissions: <p>The permissions that are granted to a specific group for accessing the FinSpace application.</p> <important> <p>When assigning application permissions, be aware that the permission <code>ManageUsersAndGroups</code> allows users to grant themselves or others access to any functionality in their FinSpace environment's application. It should only be granted to trusted users.</p> </important> <ul> <li> <p> <code>CreateDataset</code> – Group members can create new datasets.</p> </li> <li> <p> <code>ManageClusters</code> – Group members can manage Apache Spark clusters from FinSpace notebooks.</p> </li> <li> <p> <code>ManageUsersAndGroups</code> – Group members can manage users and permission groups. This is a privileged permission that allows users to grant themselves or others access to any functionality in the application. It should only be granted to trusted users.</p> </li> <li> <p> <code>ManageAttributeSets</code> – Group members can manage attribute sets.</p> </li> <li> <p> <code>ViewAuditData</code> – Group members can view audit data.</p> </li> <li> <p> <code>AccessNotebooks</code> – Group members will have access to FinSpace notebooks.</p> </li> <li> <p> <code>GetTemporaryCredentials</code> – Group members can get temporary API credentials.</p> </li> </ul>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.update_permission_group_request.UpdatePermissionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.update_permission_group_response.UpdatePermissionGroupResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.update_permission_group

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.update_permission_group.async_update_permission_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.update_permission_group_request.UpdatePermissionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["permission_group_id"] = permission_group_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if application_permissions is not None:
            input_["application_permissions"] = application_permissions
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_user(
        self,
        user_id: "aws_sdk_finspace_data.types.user_id.UserId",
        *,
        config_overrides: Optional[AsyncfinspacedataClientConfig] = None,
        type: Optional["aws_sdk_finspace_data.types.user_type.UserType"] = None,
        first_name: Optional["aws_sdk_finspace_data.types.first_name.FirstName"] = None,
        last_name: Optional["aws_sdk_finspace_data.types.last_name.LastName"] = None,
        api_access: Optional["aws_sdk_finspace_data.types.api_access.ApiAccess"] = None,
        api_access_principal_arn: Optional[
            "aws_sdk_finspace_data.types.role_arn.RoleArn"
        ] = None,
        client_token: Optional[
            "aws_sdk_finspace_data.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace_data.types.update_user_response.UpdateUserResponse":
        """<p>Modifies the details of the specified user. You cannot update the <code>userId</code> for a user.</p>

        Args:
            user_id: <p>The unique identifier for the user that you want to update.</p>
            type: <p>The option to indicate the type of user.</p> <ul> <li> <p> <code>SUPER_USER</code>– A user with permission to all the functionality and data in FinSpace.</p> </li> <li> <p> <code>APP_USER</code> – A user with specific permissions in FinSpace. The users are assigned permissions by adding them to a permission group.</p> </li> </ul>
            first_name: <p>The first name of the user.</p>
            last_name: <p>The last name of the user.</p>
            api_access: <p>The option to indicate whether the user can use the <code>GetProgrammaticAccessCredentials</code> API to obtain credentials that can then be used to access other FinSpace Data API operations.</p> <ul> <li> <p> <code>ENABLED</code> – The user has permissions to use the APIs.</p> </li> <li> <p> <code>DISABLED</code> – The user does not have permissions to use any APIs.</p> </li> </ul>
            api_access_principal_arn: <p>The ARN identifier of an AWS user or role that is allowed to call the <code>GetProgrammaticAccessCredentials</code> API to obtain a credentials token for a specific FinSpace user. This must be an IAM role within your FinSpace account.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_finspace_data.types.update_user_request.UpdateUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_finspace_data.types.update_user_response.UpdateUserResponse"
        ]:
            import aws_sdk_finspace_data._operations.aws_habanero_public_api.update_user

            (
                output,
                http_response,
            ) = await aws_sdk_finspace_data._operations.aws_habanero_public_api.update_user.async_update_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_finspace_data.types.update_user_request.UpdateUserRequest = {}  # type: ignore[typeddict-item]
        input_["user_id"] = user_id
        if type is not None:
            input_["type"] = type
        if first_name is not None:
            input_["first_name"] = first_name
        if last_name is not None:
            input_["last_name"] = last_name
        if api_access is not None:
            input_["api_access"] = api_access
        if api_access_principal_arn is not None:
            input_["api_access_principal_arn"] = api_access_principal_arn
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
