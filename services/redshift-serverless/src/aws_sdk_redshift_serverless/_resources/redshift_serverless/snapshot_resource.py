from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Optional

from aws_sdk_redshift_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.create_snapshot_copy_configuration_request
    import aws_sdk_redshift_serverless.types.create_snapshot_copy_configuration_response
    import aws_sdk_redshift_serverless.types.create_snapshot_request
    import aws_sdk_redshift_serverless.types.create_snapshot_response
    import aws_sdk_redshift_serverless.types.delete_snapshot_copy_configuration_request
    import aws_sdk_redshift_serverless.types.delete_snapshot_copy_configuration_response
    import aws_sdk_redshift_serverless.types.delete_snapshot_request
    import aws_sdk_redshift_serverless.types.delete_snapshot_response
    import aws_sdk_redshift_serverless.types.get_snapshot_request
    import aws_sdk_redshift_serverless.types.get_snapshot_response
    import aws_sdk_redshift_serverless.types.get_table_restore_status_request
    import aws_sdk_redshift_serverless.types.get_table_restore_status_response
    import aws_sdk_redshift_serverless.types.kms_key_id
    import aws_sdk_redshift_serverless.types.list_snapshot_copy_configurations_request
    import aws_sdk_redshift_serverless.types.list_snapshot_copy_configurations_response
    import aws_sdk_redshift_serverless.types.list_snapshots_request
    import aws_sdk_redshift_serverless.types.list_snapshots_response
    import aws_sdk_redshift_serverless.types.list_table_restore_status_request
    import aws_sdk_redshift_serverless.types.list_table_restore_status_response
    import aws_sdk_redshift_serverless.types.namespace_name
    import aws_sdk_redshift_serverless.types.pagination_token
    import aws_sdk_redshift_serverless.types.restore_from_snapshot_request
    import aws_sdk_redshift_serverless.types.restore_from_snapshot_response
    import aws_sdk_redshift_serverless.types.restore_table_from_snapshot_request
    import aws_sdk_redshift_serverless.types.restore_table_from_snapshot_response
    import aws_sdk_redshift_serverless.types.snapshot
    import aws_sdk_redshift_serverless.types.snapshot_copy_configuration
    import aws_sdk_redshift_serverless.types.table_restore_status
    import aws_sdk_redshift_serverless.types.tag_list
    import aws_sdk_redshift_serverless.types.update_snapshot_copy_configuration_request
    import aws_sdk_redshift_serverless.types.update_snapshot_copy_configuration_response
    import aws_sdk_redshift_serverless.types.update_snapshot_request
    import aws_sdk_redshift_serverless.types.update_snapshot_response
    import aws_sdk_redshift_serverless.types.workgroup_name
    from aws_sdk_redshift_serverless._services.async_redshift_serverless import (
        AsyncRedshiftServerlessClient,
        AsyncRedshiftServerlessClientConfig,
    )
    from aws_sdk_redshift_serverless._services.redshift_serverless import (
        RedshiftServerlessClient,
        RedshiftServerlessClientConfig,
    )


class SnapshotResource:
    def __init__(self, service: RedshiftServerlessClient) -> None:
        self._service = service

    def create_snapshot(
        self,
        namespace_name: str,
        snapshot_name: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        retention_period: Optional[int] = None,
        tags: Optional["aws_sdk_redshift_serverless.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_redshift_serverless.types.create_snapshot_response.CreateSnapshotResponse":
        r"""<p>Creates a snapshot of all databases in a namespace. For more information about snapshots, see <a href=\"https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery-points.html\"> Working with snapshots and recovery points</a>.</p>

        Args:
            namespace_name: <p>The namespace to create a snapshot for.</p>
            snapshot_name: <p>The name of the snapshot.</p>
            retention_period: <p>How long to retain the created snapshot.</p>
            tags: <p>An array of <a href=\"https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html\">Tag objects</a> to associate with the snapshot.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.create_snapshot_request.CreateSnapshotRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.create_snapshot_response.CreateSnapshotResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.create_snapshot

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.create_snapshot.create_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.create_snapshot_request.CreateSnapshotRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        input_["snapshot_name"] = snapshot_name
        if retention_period is not None:
            input_["retention_period"] = retention_period
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_snapshot_copy_configuration(
        self,
        namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName",
        destination_region: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        snapshot_retention_period: Optional[int] = None,
        destination_kms_key_id: Optional[
            "aws_sdk_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.create_snapshot_copy_configuration_response.CreateSnapshotCopyConfigurationResponse":
        """<p>Creates a snapshot copy configuration that lets you copy snapshots to another Amazon Web Services Region.</p>

        Args:
            namespace_name: <p>The name of the namespace to copy snapshots from.</p>
            destination_region: <p>The destination Amazon Web Services Region that you want to copy snapshots to.</p>
            snapshot_retention_period: <p>The retention period of the snapshots that you copy to the destination Amazon Web Services Region.</p>
            destination_kms_key_id: <p>The KMS key to use to encrypt your snapshots in the destination Amazon Web Services Region.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.create_snapshot_copy_configuration_request.CreateSnapshotCopyConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.create_snapshot_copy_configuration_response.CreateSnapshotCopyConfigurationResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.create_snapshot_copy_configuration

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.create_snapshot_copy_configuration.create_snapshot_copy_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.create_snapshot_copy_configuration_request.CreateSnapshotCopyConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        input_["destination_region"] = destination_region
        if snapshot_retention_period is not None:
            input_["snapshot_retention_period"] = snapshot_retention_period
        if destination_kms_key_id is not None:
            input_["destination_kms_key_id"] = destination_kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_snapshot(
        self,
        snapshot_name: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.delete_snapshot_response.DeleteSnapshotResponse":
        """<p>Deletes a snapshot from Amazon Redshift Serverless.</p>

        Args:
            snapshot_name: <p>The name of the snapshot to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.delete_snapshot_request.DeleteSnapshotRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.delete_snapshot_response.DeleteSnapshotResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.delete_snapshot

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.delete_snapshot.delete_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.delete_snapshot_request.DeleteSnapshotRequest = {}  # type: ignore[typeddict-item]
        input_["snapshot_name"] = snapshot_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_snapshot_copy_configuration(
        self,
        snapshot_copy_configuration_id: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.delete_snapshot_copy_configuration_response.DeleteSnapshotCopyConfigurationResponse":
        """<p>Deletes a snapshot copy configuration</p>

        Args:
            snapshot_copy_configuration_id: <p>The ID of the snapshot copy configuration to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.delete_snapshot_copy_configuration_request.DeleteSnapshotCopyConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.delete_snapshot_copy_configuration_response.DeleteSnapshotCopyConfigurationResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.delete_snapshot_copy_configuration

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.delete_snapshot_copy_configuration.delete_snapshot_copy_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.delete_snapshot_copy_configuration_request.DeleteSnapshotCopyConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["snapshot_copy_configuration_id"] = snapshot_copy_configuration_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_snapshot(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        snapshot_name: Optional[str] = None,
        owner_account: Optional[str] = None,
        snapshot_arn: Optional[str] = None,
    ) -> "aws_sdk_redshift_serverless.types.get_snapshot_response.GetSnapshotResponse":
        """<p>Returns information about a specific snapshot.</p>

        Args:
            snapshot_name: <p>The name of the snapshot to return.</p>
            owner_account: <p>The owner Amazon Web Services account of a snapshot shared with another user.</p>
            snapshot_arn: <p>The Amazon Resource Name (ARN) of the snapshot to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.get_snapshot_request.GetSnapshotRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.get_snapshot_response.GetSnapshotResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_snapshot

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.get_snapshot.get_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_snapshot_request.GetSnapshotRequest = {}  # type: ignore[typeddict-item]
        if snapshot_name is not None:
            input_["snapshot_name"] = snapshot_name
        if owner_account is not None:
            input_["owner_account"] = owner_account
        if snapshot_arn is not None:
            input_["snapshot_arn"] = snapshot_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_table_restore_status(
        self,
        table_restore_request_id: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.get_table_restore_status_response.GetTableRestoreStatusResponse":
        """<p>Returns information about a <code>TableRestoreStatus</code> object.</p>

        Args:
            table_restore_request_id: <p>The ID of the <code>RestoreTableFromSnapshot</code> request to return status for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.get_table_restore_status_request.GetTableRestoreStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.get_table_restore_status_response.GetTableRestoreStatusResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_table_restore_status

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.get_table_restore_status.get_table_restore_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_table_restore_status_request.GetTableRestoreStatusRequest = {}  # type: ignore[typeddict-item]
        input_["table_restore_request_id"] = table_restore_request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_snapshot_copy_configurations(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        namespace_name: Optional[
            "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName"
        ] = None,
        next_token: Optional[
            "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_snapshot_copy_configurations_response.ListSnapshotCopyConfigurationsResponse":
        """<p>Returns a list of snapshot copy configurations.</p>

        Args:
            namespace_name: <p>The namespace from which to list all snapshot copy configurations.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.list_snapshot_copy_configurations_request.ListSnapshotCopyConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.list_snapshot_copy_configurations_response.ListSnapshotCopyConfigurationsResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_snapshot_copy_configurations

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.list_snapshot_copy_configurations.list_snapshot_copy_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_snapshot_copy_configurations_request.ListSnapshotCopyConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_snapshots(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        namespace_name: Optional[str] = None,
        namespace_arn: Optional[str] = None,
        owner_account: Optional[str] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_snapshots_response.ListSnapshotsResponse":
        """<p>Returns a list of snapshots.</p>

        Args:
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            namespace_name: <p>The namespace from which to list all snapshots.</p>
            namespace_arn: <p>The Amazon Resource Name (ARN) of the namespace from which to list all snapshots.</p>
            owner_account: <p>The owner Amazon Web Services account of the snapshot.</p>
            start_time: <p>The time when the creation of the snapshot was initiated.</p>
            end_time: <p>The timestamp showing when the snapshot creation finished.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.list_snapshots_request.ListSnapshotsRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.list_snapshots_response.ListSnapshotsResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_snapshots

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.list_snapshots.list_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_snapshots_request.ListSnapshotsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name
        if namespace_arn is not None:
            input_["namespace_arn"] = namespace_arn
        if owner_account is not None:
            input_["owner_account"] = owner_account
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_table_restore_status(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
        namespace_name: Optional[str] = None,
        workgroup_name: Optional[str] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_table_restore_status_response.ListTableRestoreStatusResponse":
        """<p>Returns information about an array of <code>TableRestoreStatus</code> objects.</p>

        Args:
            next_token: <p>If your initial <code>ListTableRestoreStatus</code> operation returns a nextToken, you can include the returned <code>nextToken</code> in following <code>ListTableRestoreStatus</code> operations. This will return results on the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.</p>
            namespace_name: <p>The namespace from which to list all of the statuses of <code>RestoreTableFromSnapshot</code> operations .</p>
            workgroup_name: <p>The workgroup from which to list all of the statuses of <code>RestoreTableFromSnapshot</code> operations.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.list_table_restore_status_request.ListTableRestoreStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.list_table_restore_status_response.ListTableRestoreStatusResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_table_restore_status

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.list_table_restore_status.list_table_restore_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_table_restore_status_request.ListTableRestoreStatusRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def restore_from_snapshot(
        self,
        namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName",
        workgroup_name: "aws_sdk_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        snapshot_name: Optional[str] = None,
        snapshot_arn: Optional[str] = None,
        owner_account: Optional[str] = None,
        manage_admin_password: Optional[bool] = None,
        admin_password_secret_kms_key_id: Optional[
            "aws_sdk_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.restore_from_snapshot_response.RestoreFromSnapshotResponse":
        """<p>Restores a namespace from a snapshot.</p>

        Args:
            namespace_name: <p>The name of the namespace to restore the snapshot to.</p>
            workgroup_name: <p>The name of the workgroup used to restore the snapshot.</p>
            snapshot_name: <p>The name of the snapshot to restore from. Must not be specified at the same time as <code>snapshotArn</code>.</p>
            snapshot_arn: <p>The Amazon Resource Name (ARN) of the snapshot to restore from. Required if restoring from a provisioned cluster to Amazon Redshift Serverless. Must not be specified at the same time as <code>snapshotName</code>.</p> <p>The format of the ARN is arn:aws:redshift:&lt;region&gt;:&lt;account_id&gt;:snapshot:&lt;cluster_identifier&gt;/&lt;snapshot_identifier&gt;.</p>
            owner_account: <p>The Amazon Web Services account that owns the snapshot.</p>
            manage_admin_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the restored snapshot's admin credentials. If <code>MmanageAdminPassword</code> is false or not set, Amazon Redshift uses the admin credentials that the namespace or cluster had at the time the snapshot was taken.</p>
            admin_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.restore_from_snapshot_request.RestoreFromSnapshotRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.restore_from_snapshot_response.RestoreFromSnapshotResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.restore_from_snapshot

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.restore_from_snapshot.restore_from_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.restore_from_snapshot_request.RestoreFromSnapshotRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        input_["workgroup_name"] = workgroup_name
        if snapshot_name is not None:
            input_["snapshot_name"] = snapshot_name
        if snapshot_arn is not None:
            input_["snapshot_arn"] = snapshot_arn
        if owner_account is not None:
            input_["owner_account"] = owner_account
        if manage_admin_password is not None:
            input_["manage_admin_password"] = manage_admin_password
        if admin_password_secret_kms_key_id is not None:
            input_["admin_password_secret_kms_key_id"] = (
                admin_password_secret_kms_key_id
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def restore_table_from_snapshot(
        self,
        namespace_name: str,
        workgroup_name: str,
        snapshot_name: str,
        source_database_name: str,
        source_table_name: str,
        new_table_name: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        source_schema_name: Optional[str] = None,
        target_database_name: Optional[str] = None,
        target_schema_name: Optional[str] = None,
        activate_case_sensitive_identifier: Optional[bool] = None,
    ) -> "aws_sdk_redshift_serverless.types.restore_table_from_snapshot_response.RestoreTableFromSnapshotResponse":
        r"""<p>Restores a table from a snapshot to your Amazon Redshift Serverless instance. You can't use this operation to restore tables with <a href=\"https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html#t_Sorting_data-interleaved\">interleaved sort keys</a>.</p>

        Args:
            namespace_name: <p>The namespace of the snapshot to restore from.</p>
            workgroup_name: <p>The workgroup to restore the table to.</p>
            snapshot_name: <p>The name of the snapshot to restore the table from.</p>
            source_database_name: <p>The name of the source database that contains the table being restored.</p>
            source_schema_name: <p>The name of the source schema that contains the table being restored.</p>
            source_table_name: <p>The name of the source table being restored.</p>
            target_database_name: <p>The name of the database to restore the table to.</p>
            target_schema_name: <p>The name of the schema to restore the table to.</p>
            new_table_name: <p>The name of the table to create from the restore operation.</p>
            activate_case_sensitive_identifier: <p>Indicates whether name identifiers for database, schema, and table are case sensitive. If true, the names are case sensitive. If false, the names are not case sensitive. The default is false.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.restore_table_from_snapshot_request.RestoreTableFromSnapshotRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.restore_table_from_snapshot_response.RestoreTableFromSnapshotResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.restore_table_from_snapshot

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.restore_table_from_snapshot.restore_table_from_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.restore_table_from_snapshot_request.RestoreTableFromSnapshotRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        input_["workgroup_name"] = workgroup_name
        input_["snapshot_name"] = snapshot_name
        input_["source_database_name"] = source_database_name
        if source_schema_name is not None:
            input_["source_schema_name"] = source_schema_name
        input_["source_table_name"] = source_table_name
        if target_database_name is not None:
            input_["target_database_name"] = target_database_name
        if target_schema_name is not None:
            input_["target_schema_name"] = target_schema_name
        input_["new_table_name"] = new_table_name
        if activate_case_sensitive_identifier is not None:
            input_["activate_case_sensitive_identifier"] = (
                activate_case_sensitive_identifier
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_snapshot(
        self,
        snapshot_name: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        retention_period: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.update_snapshot_response.UpdateSnapshotResponse":
        """<p>Updates a snapshot.</p>

        Args:
            snapshot_name: <p>The name of the snapshot.</p>
            retention_period: <p>The new retention period of the snapshot.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.update_snapshot_request.UpdateSnapshotRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.update_snapshot_response.UpdateSnapshotResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.update_snapshot

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.update_snapshot.update_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.update_snapshot_request.UpdateSnapshotRequest = {}  # type: ignore[typeddict-item]
        input_["snapshot_name"] = snapshot_name
        if retention_period is not None:
            input_["retention_period"] = retention_period

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_snapshot_copy_configuration(
        self,
        snapshot_copy_configuration_id: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        snapshot_retention_period: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.update_snapshot_copy_configuration_response.UpdateSnapshotCopyConfigurationResponse":
        """<p>Updates a snapshot copy configuration.</p>

        Args:
            snapshot_copy_configuration_id: <p>The ID of the snapshot copy configuration to update.</p>
            snapshot_retention_period: <p>The new retention period of how long to keep a snapshot in the destination Amazon Web Services Region.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.update_snapshot_copy_configuration_request.UpdateSnapshotCopyConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.update_snapshot_copy_configuration_response.UpdateSnapshotCopyConfigurationResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.update_snapshot_copy_configuration

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.update_snapshot_copy_configuration.update_snapshot_copy_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.update_snapshot_copy_configuration_request.UpdateSnapshotCopyConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["snapshot_copy_configuration_id"] = snapshot_copy_configuration_id
        if snapshot_retention_period is not None:
            input_["snapshot_retention_period"] = snapshot_retention_period

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncSnapshotResource:
    def __init__(self, service: AsyncRedshiftServerlessClient) -> None:
        self._service = service

    async def create_snapshot(
        self,
        namespace_name: str,
        snapshot_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        retention_period: Optional[int] = None,
        tags: Optional["aws_sdk_redshift_serverless.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_redshift_serverless.types.create_snapshot_response.CreateSnapshotResponse":
        r"""<p>Creates a snapshot of all databases in a namespace. For more information about snapshots, see <a href=\"https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery-points.html\"> Working with snapshots and recovery points</a>.</p>

        Args:
            namespace_name: <p>The namespace to create a snapshot for.</p>
            snapshot_name: <p>The name of the snapshot.</p>
            retention_period: <p>How long to retain the created snapshot.</p>
            tags: <p>An array of <a href=\"https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html\">Tag objects</a> to associate with the snapshot.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.create_snapshot_request.CreateSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.create_snapshot_response.CreateSnapshotResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.create_snapshot

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.create_snapshot.async_create_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.create_snapshot_request.CreateSnapshotRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        input_["snapshot_name"] = snapshot_name
        if retention_period is not None:
            input_["retention_period"] = retention_period
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_snapshot_copy_configuration(
        self,
        namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName",
        destination_region: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        snapshot_retention_period: Optional[int] = None,
        destination_kms_key_id: Optional[
            "aws_sdk_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.create_snapshot_copy_configuration_response.CreateSnapshotCopyConfigurationResponse":
        """<p>Creates a snapshot copy configuration that lets you copy snapshots to another Amazon Web Services Region.</p>

        Args:
            namespace_name: <p>The name of the namespace to copy snapshots from.</p>
            destination_region: <p>The destination Amazon Web Services Region that you want to copy snapshots to.</p>
            snapshot_retention_period: <p>The retention period of the snapshots that you copy to the destination Amazon Web Services Region.</p>
            destination_kms_key_id: <p>The KMS key to use to encrypt your snapshots in the destination Amazon Web Services Region.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.create_snapshot_copy_configuration_request.CreateSnapshotCopyConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.create_snapshot_copy_configuration_response.CreateSnapshotCopyConfigurationResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.create_snapshot_copy_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.create_snapshot_copy_configuration.async_create_snapshot_copy_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.create_snapshot_copy_configuration_request.CreateSnapshotCopyConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        input_["destination_region"] = destination_region
        if snapshot_retention_period is not None:
            input_["snapshot_retention_period"] = snapshot_retention_period
        if destination_kms_key_id is not None:
            input_["destination_kms_key_id"] = destination_kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_snapshot(
        self,
        snapshot_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.delete_snapshot_response.DeleteSnapshotResponse":
        """<p>Deletes a snapshot from Amazon Redshift Serverless.</p>

        Args:
            snapshot_name: <p>The name of the snapshot to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.delete_snapshot_request.DeleteSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.delete_snapshot_response.DeleteSnapshotResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.delete_snapshot

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.delete_snapshot.async_delete_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.delete_snapshot_request.DeleteSnapshotRequest = {}  # type: ignore[typeddict-item]
        input_["snapshot_name"] = snapshot_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_snapshot_copy_configuration(
        self,
        snapshot_copy_configuration_id: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.delete_snapshot_copy_configuration_response.DeleteSnapshotCopyConfigurationResponse":
        """<p>Deletes a snapshot copy configuration</p>

        Args:
            snapshot_copy_configuration_id: <p>The ID of the snapshot copy configuration to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.delete_snapshot_copy_configuration_request.DeleteSnapshotCopyConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.delete_snapshot_copy_configuration_response.DeleteSnapshotCopyConfigurationResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.delete_snapshot_copy_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.delete_snapshot_copy_configuration.async_delete_snapshot_copy_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.delete_snapshot_copy_configuration_request.DeleteSnapshotCopyConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["snapshot_copy_configuration_id"] = snapshot_copy_configuration_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        snapshot_name: Optional[str] = None,
        owner_account: Optional[str] = None,
        snapshot_arn: Optional[str] = None,
    ) -> "aws_sdk_redshift_serverless.types.get_snapshot_response.GetSnapshotResponse":
        """<p>Returns information about a specific snapshot.</p>

        Args:
            snapshot_name: <p>The name of the snapshot to return.</p>
            owner_account: <p>The owner Amazon Web Services account of a snapshot shared with another user.</p>
            snapshot_arn: <p>The Amazon Resource Name (ARN) of the snapshot to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.get_snapshot_request.GetSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.get_snapshot_response.GetSnapshotResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_snapshot

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.get_snapshot.async_get_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_snapshot_request.GetSnapshotRequest = {}  # type: ignore[typeddict-item]
        if snapshot_name is not None:
            input_["snapshot_name"] = snapshot_name
        if owner_account is not None:
            input_["owner_account"] = owner_account
        if snapshot_arn is not None:
            input_["snapshot_arn"] = snapshot_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table_restore_status(
        self,
        table_restore_request_id: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.get_table_restore_status_response.GetTableRestoreStatusResponse":
        """<p>Returns information about a <code>TableRestoreStatus</code> object.</p>

        Args:
            table_restore_request_id: <p>The ID of the <code>RestoreTableFromSnapshot</code> request to return status for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.get_table_restore_status_request.GetTableRestoreStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.get_table_restore_status_response.GetTableRestoreStatusResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_table_restore_status

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.get_table_restore_status.async_get_table_restore_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_table_restore_status_request.GetTableRestoreStatusRequest = {}  # type: ignore[typeddict-item]
        input_["table_restore_request_id"] = table_restore_request_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_snapshot_copy_configurations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        namespace_name: Optional[
            "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName"
        ] = None,
        next_token: Optional[
            "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_snapshot_copy_configurations_response.ListSnapshotCopyConfigurationsResponse":
        """<p>Returns a list of snapshot copy configurations.</p>

        Args:
            namespace_name: <p>The namespace from which to list all snapshot copy configurations.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.list_snapshot_copy_configurations_request.ListSnapshotCopyConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.list_snapshot_copy_configurations_response.ListSnapshotCopyConfigurationsResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_snapshot_copy_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.list_snapshot_copy_configurations.async_list_snapshot_copy_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_snapshot_copy_configurations_request.ListSnapshotCopyConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name
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

    async def list_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        namespace_name: Optional[str] = None,
        namespace_arn: Optional[str] = None,
        owner_account: Optional[str] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_snapshots_response.ListSnapshotsResponse":
        """<p>Returns a list of snapshots.</p>

        Args:
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            namespace_name: <p>The namespace from which to list all snapshots.</p>
            namespace_arn: <p>The Amazon Resource Name (ARN) of the namespace from which to list all snapshots.</p>
            owner_account: <p>The owner Amazon Web Services account of the snapshot.</p>
            start_time: <p>The time when the creation of the snapshot was initiated.</p>
            end_time: <p>The timestamp showing when the snapshot creation finished.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.list_snapshots_request.ListSnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.list_snapshots_response.ListSnapshotsResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_snapshots

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.list_snapshots.async_list_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_snapshots_request.ListSnapshotsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name
        if namespace_arn is not None:
            input_["namespace_arn"] = namespace_arn
        if owner_account is not None:
            input_["owner_account"] = owner_account
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_table_restore_status(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
        namespace_name: Optional[str] = None,
        workgroup_name: Optional[str] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_table_restore_status_response.ListTableRestoreStatusResponse":
        """<p>Returns information about an array of <code>TableRestoreStatus</code> objects.</p>

        Args:
            next_token: <p>If your initial <code>ListTableRestoreStatus</code> operation returns a nextToken, you can include the returned <code>nextToken</code> in following <code>ListTableRestoreStatus</code> operations. This will return results on the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.</p>
            namespace_name: <p>The namespace from which to list all of the statuses of <code>RestoreTableFromSnapshot</code> operations .</p>
            workgroup_name: <p>The workgroup from which to list all of the statuses of <code>RestoreTableFromSnapshot</code> operations.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.list_table_restore_status_request.ListTableRestoreStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.list_table_restore_status_response.ListTableRestoreStatusResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_table_restore_status

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.list_table_restore_status.async_list_table_restore_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_table_restore_status_request.ListTableRestoreStatusRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def restore_from_snapshot(
        self,
        namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName",
        workgroup_name: "aws_sdk_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        snapshot_name: Optional[str] = None,
        snapshot_arn: Optional[str] = None,
        owner_account: Optional[str] = None,
        manage_admin_password: Optional[bool] = None,
        admin_password_secret_kms_key_id: Optional[
            "aws_sdk_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.restore_from_snapshot_response.RestoreFromSnapshotResponse":
        """<p>Restores a namespace from a snapshot.</p>

        Args:
            namespace_name: <p>The name of the namespace to restore the snapshot to.</p>
            workgroup_name: <p>The name of the workgroup used to restore the snapshot.</p>
            snapshot_name: <p>The name of the snapshot to restore from. Must not be specified at the same time as <code>snapshotArn</code>.</p>
            snapshot_arn: <p>The Amazon Resource Name (ARN) of the snapshot to restore from. Required if restoring from a provisioned cluster to Amazon Redshift Serverless. Must not be specified at the same time as <code>snapshotName</code>.</p> <p>The format of the ARN is arn:aws:redshift:&lt;region&gt;:&lt;account_id&gt;:snapshot:&lt;cluster_identifier&gt;/&lt;snapshot_identifier&gt;.</p>
            owner_account: <p>The Amazon Web Services account that owns the snapshot.</p>
            manage_admin_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the restored snapshot's admin credentials. If <code>MmanageAdminPassword</code> is false or not set, Amazon Redshift uses the admin credentials that the namespace or cluster had at the time the snapshot was taken.</p>
            admin_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.restore_from_snapshot_request.RestoreFromSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.restore_from_snapshot_response.RestoreFromSnapshotResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.restore_from_snapshot

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.restore_from_snapshot.async_restore_from_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.restore_from_snapshot_request.RestoreFromSnapshotRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        input_["workgroup_name"] = workgroup_name
        if snapshot_name is not None:
            input_["snapshot_name"] = snapshot_name
        if snapshot_arn is not None:
            input_["snapshot_arn"] = snapshot_arn
        if owner_account is not None:
            input_["owner_account"] = owner_account
        if manage_admin_password is not None:
            input_["manage_admin_password"] = manage_admin_password
        if admin_password_secret_kms_key_id is not None:
            input_["admin_password_secret_kms_key_id"] = (
                admin_password_secret_kms_key_id
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def restore_table_from_snapshot(
        self,
        namespace_name: str,
        workgroup_name: str,
        snapshot_name: str,
        source_database_name: str,
        source_table_name: str,
        new_table_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        source_schema_name: Optional[str] = None,
        target_database_name: Optional[str] = None,
        target_schema_name: Optional[str] = None,
        activate_case_sensitive_identifier: Optional[bool] = None,
    ) -> "aws_sdk_redshift_serverless.types.restore_table_from_snapshot_response.RestoreTableFromSnapshotResponse":
        r"""<p>Restores a table from a snapshot to your Amazon Redshift Serverless instance. You can't use this operation to restore tables with <a href=\"https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html#t_Sorting_data-interleaved\">interleaved sort keys</a>.</p>

        Args:
            namespace_name: <p>The namespace of the snapshot to restore from.</p>
            workgroup_name: <p>The workgroup to restore the table to.</p>
            snapshot_name: <p>The name of the snapshot to restore the table from.</p>
            source_database_name: <p>The name of the source database that contains the table being restored.</p>
            source_schema_name: <p>The name of the source schema that contains the table being restored.</p>
            source_table_name: <p>The name of the source table being restored.</p>
            target_database_name: <p>The name of the database to restore the table to.</p>
            target_schema_name: <p>The name of the schema to restore the table to.</p>
            new_table_name: <p>The name of the table to create from the restore operation.</p>
            activate_case_sensitive_identifier: <p>Indicates whether name identifiers for database, schema, and table are case sensitive. If true, the names are case sensitive. If false, the names are not case sensitive. The default is false.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.restore_table_from_snapshot_request.RestoreTableFromSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.restore_table_from_snapshot_response.RestoreTableFromSnapshotResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.restore_table_from_snapshot

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.restore_table_from_snapshot.async_restore_table_from_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.restore_table_from_snapshot_request.RestoreTableFromSnapshotRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        input_["workgroup_name"] = workgroup_name
        input_["snapshot_name"] = snapshot_name
        input_["source_database_name"] = source_database_name
        if source_schema_name is not None:
            input_["source_schema_name"] = source_schema_name
        input_["source_table_name"] = source_table_name
        if target_database_name is not None:
            input_["target_database_name"] = target_database_name
        if target_schema_name is not None:
            input_["target_schema_name"] = target_schema_name
        input_["new_table_name"] = new_table_name
        if activate_case_sensitive_identifier is not None:
            input_["activate_case_sensitive_identifier"] = (
                activate_case_sensitive_identifier
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_snapshot(
        self,
        snapshot_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        retention_period: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.update_snapshot_response.UpdateSnapshotResponse":
        """<p>Updates a snapshot.</p>

        Args:
            snapshot_name: <p>The name of the snapshot.</p>
            retention_period: <p>The new retention period of the snapshot.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.update_snapshot_request.UpdateSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.update_snapshot_response.UpdateSnapshotResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.update_snapshot

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.update_snapshot.async_update_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.update_snapshot_request.UpdateSnapshotRequest = {}  # type: ignore[typeddict-item]
        input_["snapshot_name"] = snapshot_name
        if retention_period is not None:
            input_["retention_period"] = retention_period

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_snapshot_copy_configuration(
        self,
        snapshot_copy_configuration_id: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        snapshot_retention_period: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.update_snapshot_copy_configuration_response.UpdateSnapshotCopyConfigurationResponse":
        """<p>Updates a snapshot copy configuration.</p>

        Args:
            snapshot_copy_configuration_id: <p>The ID of the snapshot copy configuration to update.</p>
            snapshot_retention_period: <p>The new retention period of how long to keep a snapshot in the destination Amazon Web Services Region.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.update_snapshot_copy_configuration_request.UpdateSnapshotCopyConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.update_snapshot_copy_configuration_response.UpdateSnapshotCopyConfigurationResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.update_snapshot_copy_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.update_snapshot_copy_configuration.async_update_snapshot_copy_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.update_snapshot_copy_configuration_request.UpdateSnapshotCopyConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["snapshot_copy_configuration_id"] = snapshot_copy_configuration_id
        if snapshot_retention_period is not None:
            input_["snapshot_retention_period"] = snapshot_retention_period

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
