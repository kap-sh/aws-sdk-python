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
    import aws_sdk_redshift_serverless.types.catalog_name_string
    import aws_sdk_redshift_serverless.types.create_namespace_request
    import aws_sdk_redshift_serverless.types.create_namespace_response
    import aws_sdk_redshift_serverless.types.db_password
    import aws_sdk_redshift_serverless.types.db_user
    import aws_sdk_redshift_serverless.types.delete_namespace_request
    import aws_sdk_redshift_serverless.types.delete_namespace_response
    import aws_sdk_redshift_serverless.types.get_namespace_request
    import aws_sdk_redshift_serverless.types.get_namespace_response
    import aws_sdk_redshift_serverless.types.iam_role_arn_list
    import aws_sdk_redshift_serverless.types.kms_key_id
    import aws_sdk_redshift_serverless.types.lakehouse_idc_registration
    import aws_sdk_redshift_serverless.types.lakehouse_registration
    import aws_sdk_redshift_serverless.types.list_namespaces_request
    import aws_sdk_redshift_serverless.types.list_namespaces_response
    import aws_sdk_redshift_serverless.types.log_export_list
    import aws_sdk_redshift_serverless.types.namespace
    import aws_sdk_redshift_serverless.types.namespace_name
    import aws_sdk_redshift_serverless.types.redshift_idc_application_arn
    import aws_sdk_redshift_serverless.types.tag_list
    import aws_sdk_redshift_serverless.types.update_lakehouse_configuration_request
    import aws_sdk_redshift_serverless.types.update_lakehouse_configuration_response
    import aws_sdk_redshift_serverless.types.update_namespace_request
    import aws_sdk_redshift_serverless.types.update_namespace_response
    from aws_sdk_redshift_serverless._services.async_redshift_serverless import (
        AsyncRedshiftServerlessClient,
        AsyncRedshiftServerlessClientConfig,
    )
    from aws_sdk_redshift_serverless._services.redshift_serverless import (
        RedshiftServerlessClient,
        RedshiftServerlessClientConfig,
    )


class NamespaceResource:
    def __init__(self, service: RedshiftServerlessClient) -> None:
        self._service = service

    def put(
        self,
        namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        admin_username: Optional[
            "aws_sdk_redshift_serverless.types.db_user.DbUser"
        ] = None,
        admin_user_password: Optional[
            "aws_sdk_redshift_serverless.types.db_password.DbPassword"
        ] = None,
        db_name: Optional[str] = None,
        kms_key_id: Optional[str] = None,
        default_iam_role_arn: Optional[str] = None,
        iam_roles: Optional[
            "aws_sdk_redshift_serverless.types.iam_role_arn_list.IamRoleArnList"
        ] = None,
        log_exports: Optional[
            "aws_sdk_redshift_serverless.types.log_export_list.LogExportList"
        ] = None,
        tags: Optional["aws_sdk_redshift_serverless.types.tag_list.TagList"] = None,
        manage_admin_password: Optional[bool] = None,
        admin_password_secret_kms_key_id: Optional[
            "aws_sdk_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
        redshift_idc_application_arn: Optional[
            "aws_sdk_redshift_serverless.types.redshift_idc_application_arn.RedshiftIdcApplicationArn"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.create_namespace_response.CreateNamespaceResponse":
        """<p>Creates a namespace in Amazon Redshift Serverless.</p>

        Args:
            namespace_name: <p>The name of the namespace.</p>
            admin_username: <p>The username of the administrator for the first database created in the namespace.</p>
            admin_user_password: <p>The password of the administrator for the first database created in the namespace.</p> <p>You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. </p>
            db_name: <p>The name of the first database created in the namespace.</p>
            kms_key_id: <p>The ID of the Amazon Web Services Key Management Service key used to encrypt your data.</p>
            default_iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.</p>
            iam_roles: <p>A list of IAM roles to associate with the namespace.</p>
            log_exports: <p>The types of logs the namespace can export. Available export types are <code>userlog</code>, <code>connectionlog</code>, and <code>useractivitylog</code>.</p>
            tags: <p>A list of tag instances.</p>
            manage_admin_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the namespace's admin credentials. You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. If <code>manageAdminPassword</code> is false or not set, Amazon Redshift uses <code>adminUserPassword</code> for the admin user account's password. </p>
            admin_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if <code>manageAdminPassword</code> is true.</p>
            redshift_idc_application_arn: <p>The ARN for the Redshift application that integrates with IAM Identity Center.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.create_namespace_request.CreateNamespaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.create_namespace_response.CreateNamespaceResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.create_namespace

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.create_namespace.create_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.create_namespace_request.CreateNamespaceRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        if admin_username is not None:
            input_["admin_username"] = admin_username
        if admin_user_password is not None:
            input_["admin_user_password"] = admin_user_password
        if db_name is not None:
            input_["db_name"] = db_name
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if default_iam_role_arn is not None:
            input_["default_iam_role_arn"] = default_iam_role_arn
        if iam_roles is not None:
            input_["iam_roles"] = iam_roles
        if log_exports is not None:
            input_["log_exports"] = log_exports
        if tags is not None:
            input_["tags"] = tags
        if manage_admin_password is not None:
            input_["manage_admin_password"] = manage_admin_password
        if admin_password_secret_kms_key_id is not None:
            input_["admin_password_secret_kms_key_id"] = (
                admin_password_secret_kms_key_id
            )
        if redshift_idc_application_arn is not None:
            input_["redshift_idc_application_arn"] = redshift_idc_application_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> (
        "aws_sdk_redshift_serverless.types.get_namespace_response.GetNamespaceResponse"
    ):
        """<p>Returns information about a namespace in Amazon Redshift Serverless.</p>

        Args:
            namespace_name: <p>The name of the namespace to retrieve information for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.get_namespace_request.GetNamespaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.get_namespace_response.GetNamespaceResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_namespace

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.get_namespace.get_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_namespace_request.GetNamespaceRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        admin_user_password: Optional[
            "aws_sdk_redshift_serverless.types.db_password.DbPassword"
        ] = None,
        admin_username: Optional[
            "aws_sdk_redshift_serverless.types.db_user.DbUser"
        ] = None,
        kms_key_id: Optional[str] = None,
        default_iam_role_arn: Optional[str] = None,
        iam_roles: Optional[
            "aws_sdk_redshift_serverless.types.iam_role_arn_list.IamRoleArnList"
        ] = None,
        log_exports: Optional[
            "aws_sdk_redshift_serverless.types.log_export_list.LogExportList"
        ] = None,
        manage_admin_password: Optional[bool] = None,
        admin_password_secret_kms_key_id: Optional[
            "aws_sdk_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.update_namespace_response.UpdateNamespaceResponse":
        """<p>Updates a namespace with the specified settings. Unless required, you can't update multiple parameters in one request. For example, you must specify both <code>adminUsername</code> and <code>adminUserPassword</code> to update either field, but you can't update both <code>kmsKeyId</code> and <code>logExports</code> in a single request.</p>

        Args:
            namespace_name: <p>The name of the namespace to update. You can't update the name of a namespace once it is created.</p>
            admin_user_password: <p>The password of the administrator for the first database created in the namespace. This parameter must be updated together with <code>adminUsername</code>.</p> <p>You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. </p>
            admin_username: <p>The username of the administrator for the first database created in the namespace. This parameter must be updated together with <code>adminUserPassword</code>.</p>
            kms_key_id: <p>The ID of the Amazon Web Services Key Management Service key used to encrypt your data.</p>
            default_iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. This parameter must be updated together with <code>iamRoles</code>.</p>
            iam_roles: <p>A list of IAM roles to associate with the namespace. This parameter must be updated together with <code>defaultIamRoleArn</code>.</p>
            log_exports: <p>The types of logs the namespace can export. The export types are <code>userlog</code>, <code>connectionlog</code>, and <code>useractivitylog</code>.</p>
            manage_admin_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the namespace's admin credentials. You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. If <code>manageAdminPassword</code> is false or not set, Amazon Redshift uses <code>adminUserPassword</code> for the admin user account's password. </p>
            admin_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if <code>manageAdminPassword</code> is true.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.update_namespace_request.UpdateNamespaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.update_namespace_response.UpdateNamespaceResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.update_namespace

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.update_namespace.update_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.update_namespace_request.UpdateNamespaceRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        if admin_user_password is not None:
            input_["admin_user_password"] = admin_user_password
        if admin_username is not None:
            input_["admin_username"] = admin_username
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if default_iam_role_arn is not None:
            input_["default_iam_role_arn"] = default_iam_role_arn
        if iam_roles is not None:
            input_["iam_roles"] = iam_roles
        if log_exports is not None:
            input_["log_exports"] = log_exports
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

    def delete(
        self,
        namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        final_snapshot_name: Optional[str] = None,
        final_snapshot_retention_period: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.delete_namespace_response.DeleteNamespaceResponse":
        """<p>Deletes a namespace from Amazon Redshift Serverless. Before you delete the namespace, you can create a final snapshot that has all of the data within the namespace.</p>

        Args:
            namespace_name: <p>The name of the namespace to delete.</p>
            final_snapshot_name: <p>The name of the snapshot to be created before the namespace is deleted.</p>
            final_snapshot_retention_period: <p>How long to retain the final snapshot.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.delete_namespace_request.DeleteNamespaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.delete_namespace_response.DeleteNamespaceResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.delete_namespace

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.delete_namespace.delete_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.delete_namespace_request.DeleteNamespaceRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        if final_snapshot_name is not None:
            input_["final_snapshot_name"] = final_snapshot_name
        if final_snapshot_retention_period is not None:
            input_["final_snapshot_retention_period"] = final_snapshot_retention_period

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_namespaces_response.ListNamespacesResponse":
        """<p>Returns information about a list of specified namespaces.</p>

        Args:
            next_token: <p>If your initial <code>ListNamespaces</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListNamespaces</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.list_namespaces_request.ListNamespacesRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.list_namespaces_response.ListNamespacesResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_namespaces

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.list_namespaces.list_namespaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_namespaces_request.ListNamespacesRequest = {}  # type: ignore[typeddict-item]
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

    def update_lakehouse_configuration(
        self,
        namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        lakehouse_registration: Optional[
            "aws_sdk_redshift_serverless.types.lakehouse_registration.LakehouseRegistration"
        ] = None,
        catalog_name: Optional[
            "aws_sdk_redshift_serverless.types.catalog_name_string.CatalogNameString"
        ] = None,
        lakehouse_idc_registration: Optional[
            "aws_sdk_redshift_serverless.types.lakehouse_idc_registration.LakehouseIdcRegistration"
        ] = None,
        lakehouse_idc_application_arn: Optional[str] = None,
        dry_run: Optional[bool] = None,
    ) -> "aws_sdk_redshift_serverless.types.update_lakehouse_configuration_response.UpdateLakehouseConfigurationResponse":
        """<p>Modifies the lakehouse configuration for a namespace. This operation allows you to manage Amazon Redshift federated permissions and Amazon Web Services IAM Identity Center trusted identity propagation.</p>

        Args:
            namespace_name: <p>The name of the namespace whose lakehouse configuration you want to modify.</p>
            lakehouse_registration: <p>Specifies whether to register or deregister the namespace with Amazon Redshift federated permissions. Valid values are <code>Register</code> or <code>Deregister</code>.</p>
            catalog_name: <p>The name of the Glue Data Catalog that will be associated with the namespace enabled with Amazon Redshift federated permissions.</p> <p>Pattern: <code>^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$</code> </p>
            lakehouse_idc_registration: <p>Modifies the Amazon Web Services IAM Identity Center trusted identity propagation on a namespace enabled with Amazon Redshift federated permissions. Valid values are <code>Associate</code> or <code>Disassociate</code>.</p>
            lakehouse_idc_application_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling Amazon Web Services IAM Identity Center trusted identity propagation on a namespace enabled with Amazon Redshift federated permissions.</p>
            dry_run: <p>A boolean value that, if <code>true</code>, validates the request without actually updating the lakehouse configuration. Use this to check for errors before making changes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.update_lakehouse_configuration_request.UpdateLakehouseConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.update_lakehouse_configuration_response.UpdateLakehouseConfigurationResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.update_lakehouse_configuration

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.update_lakehouse_configuration.update_lakehouse_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.update_lakehouse_configuration_request.UpdateLakehouseConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        if lakehouse_registration is not None:
            input_["lakehouse_registration"] = lakehouse_registration
        if catalog_name is not None:
            input_["catalog_name"] = catalog_name
        if lakehouse_idc_registration is not None:
            input_["lakehouse_idc_registration"] = lakehouse_idc_registration
        if lakehouse_idc_application_arn is not None:
            input_["lakehouse_idc_application_arn"] = lakehouse_idc_application_arn
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncNamespaceResource:
    def __init__(self, service: AsyncRedshiftServerlessClient) -> None:
        self._service = service

    async def put(
        self,
        namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        admin_username: Optional[
            "aws_sdk_redshift_serverless.types.db_user.DbUser"
        ] = None,
        admin_user_password: Optional[
            "aws_sdk_redshift_serverless.types.db_password.DbPassword"
        ] = None,
        db_name: Optional[str] = None,
        kms_key_id: Optional[str] = None,
        default_iam_role_arn: Optional[str] = None,
        iam_roles: Optional[
            "aws_sdk_redshift_serverless.types.iam_role_arn_list.IamRoleArnList"
        ] = None,
        log_exports: Optional[
            "aws_sdk_redshift_serverless.types.log_export_list.LogExportList"
        ] = None,
        tags: Optional["aws_sdk_redshift_serverless.types.tag_list.TagList"] = None,
        manage_admin_password: Optional[bool] = None,
        admin_password_secret_kms_key_id: Optional[
            "aws_sdk_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
        redshift_idc_application_arn: Optional[
            "aws_sdk_redshift_serverless.types.redshift_idc_application_arn.RedshiftIdcApplicationArn"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.create_namespace_response.CreateNamespaceResponse":
        """<p>Creates a namespace in Amazon Redshift Serverless.</p>

        Args:
            namespace_name: <p>The name of the namespace.</p>
            admin_username: <p>The username of the administrator for the first database created in the namespace.</p>
            admin_user_password: <p>The password of the administrator for the first database created in the namespace.</p> <p>You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. </p>
            db_name: <p>The name of the first database created in the namespace.</p>
            kms_key_id: <p>The ID of the Amazon Web Services Key Management Service key used to encrypt your data.</p>
            default_iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.</p>
            iam_roles: <p>A list of IAM roles to associate with the namespace.</p>
            log_exports: <p>The types of logs the namespace can export. Available export types are <code>userlog</code>, <code>connectionlog</code>, and <code>useractivitylog</code>.</p>
            tags: <p>A list of tag instances.</p>
            manage_admin_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the namespace's admin credentials. You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. If <code>manageAdminPassword</code> is false or not set, Amazon Redshift uses <code>adminUserPassword</code> for the admin user account's password. </p>
            admin_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if <code>manageAdminPassword</code> is true.</p>
            redshift_idc_application_arn: <p>The ARN for the Redshift application that integrates with IAM Identity Center.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.create_namespace_request.CreateNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.create_namespace_response.CreateNamespaceResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.create_namespace

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.create_namespace.async_create_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.create_namespace_request.CreateNamespaceRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        if admin_username is not None:
            input_["admin_username"] = admin_username
        if admin_user_password is not None:
            input_["admin_user_password"] = admin_user_password
        if db_name is not None:
            input_["db_name"] = db_name
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if default_iam_role_arn is not None:
            input_["default_iam_role_arn"] = default_iam_role_arn
        if iam_roles is not None:
            input_["iam_roles"] = iam_roles
        if log_exports is not None:
            input_["log_exports"] = log_exports
        if tags is not None:
            input_["tags"] = tags
        if manage_admin_password is not None:
            input_["manage_admin_password"] = manage_admin_password
        if admin_password_secret_kms_key_id is not None:
            input_["admin_password_secret_kms_key_id"] = (
                admin_password_secret_kms_key_id
            )
        if redshift_idc_application_arn is not None:
            input_["redshift_idc_application_arn"] = redshift_idc_application_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> (
        "aws_sdk_redshift_serverless.types.get_namespace_response.GetNamespaceResponse"
    ):
        """<p>Returns information about a namespace in Amazon Redshift Serverless.</p>

        Args:
            namespace_name: <p>The name of the namespace to retrieve information for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.get_namespace_request.GetNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.get_namespace_response.GetNamespaceResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_namespace

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.get_namespace.async_get_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_namespace_request.GetNamespaceRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        admin_user_password: Optional[
            "aws_sdk_redshift_serverless.types.db_password.DbPassword"
        ] = None,
        admin_username: Optional[
            "aws_sdk_redshift_serverless.types.db_user.DbUser"
        ] = None,
        kms_key_id: Optional[str] = None,
        default_iam_role_arn: Optional[str] = None,
        iam_roles: Optional[
            "aws_sdk_redshift_serverless.types.iam_role_arn_list.IamRoleArnList"
        ] = None,
        log_exports: Optional[
            "aws_sdk_redshift_serverless.types.log_export_list.LogExportList"
        ] = None,
        manage_admin_password: Optional[bool] = None,
        admin_password_secret_kms_key_id: Optional[
            "aws_sdk_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.update_namespace_response.UpdateNamespaceResponse":
        """<p>Updates a namespace with the specified settings. Unless required, you can't update multiple parameters in one request. For example, you must specify both <code>adminUsername</code> and <code>adminUserPassword</code> to update either field, but you can't update both <code>kmsKeyId</code> and <code>logExports</code> in a single request.</p>

        Args:
            namespace_name: <p>The name of the namespace to update. You can't update the name of a namespace once it is created.</p>
            admin_user_password: <p>The password of the administrator for the first database created in the namespace. This parameter must be updated together with <code>adminUsername</code>.</p> <p>You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. </p>
            admin_username: <p>The username of the administrator for the first database created in the namespace. This parameter must be updated together with <code>adminUserPassword</code>.</p>
            kms_key_id: <p>The ID of the Amazon Web Services Key Management Service key used to encrypt your data.</p>
            default_iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. This parameter must be updated together with <code>iamRoles</code>.</p>
            iam_roles: <p>A list of IAM roles to associate with the namespace. This parameter must be updated together with <code>defaultIamRoleArn</code>.</p>
            log_exports: <p>The types of logs the namespace can export. The export types are <code>userlog</code>, <code>connectionlog</code>, and <code>useractivitylog</code>.</p>
            manage_admin_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the namespace's admin credentials. You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. If <code>manageAdminPassword</code> is false or not set, Amazon Redshift uses <code>adminUserPassword</code> for the admin user account's password. </p>
            admin_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if <code>manageAdminPassword</code> is true.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.update_namespace_request.UpdateNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.update_namespace_response.UpdateNamespaceResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.update_namespace

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.update_namespace.async_update_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.update_namespace_request.UpdateNamespaceRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        if admin_user_password is not None:
            input_["admin_user_password"] = admin_user_password
        if admin_username is not None:
            input_["admin_username"] = admin_username
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if default_iam_role_arn is not None:
            input_["default_iam_role_arn"] = default_iam_role_arn
        if iam_roles is not None:
            input_["iam_roles"] = iam_roles
        if log_exports is not None:
            input_["log_exports"] = log_exports
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

    async def delete(
        self,
        namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        final_snapshot_name: Optional[str] = None,
        final_snapshot_retention_period: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.delete_namespace_response.DeleteNamespaceResponse":
        """<p>Deletes a namespace from Amazon Redshift Serverless. Before you delete the namespace, you can create a final snapshot that has all of the data within the namespace.</p>

        Args:
            namespace_name: <p>The name of the namespace to delete.</p>
            final_snapshot_name: <p>The name of the snapshot to be created before the namespace is deleted.</p>
            final_snapshot_retention_period: <p>How long to retain the final snapshot.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.delete_namespace_request.DeleteNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.delete_namespace_response.DeleteNamespaceResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.delete_namespace

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.delete_namespace.async_delete_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.delete_namespace_request.DeleteNamespaceRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        if final_snapshot_name is not None:
            input_["final_snapshot_name"] = final_snapshot_name
        if final_snapshot_retention_period is not None:
            input_["final_snapshot_retention_period"] = final_snapshot_retention_period

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_namespaces_response.ListNamespacesResponse":
        """<p>Returns information about a list of specified namespaces.</p>

        Args:
            next_token: <p>If your initial <code>ListNamespaces</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListNamespaces</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.list_namespaces_request.ListNamespacesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.list_namespaces_response.ListNamespacesResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_namespaces

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.list_namespaces.async_list_namespaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_namespaces_request.ListNamespacesRequest = {}  # type: ignore[typeddict-item]
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

    async def update_lakehouse_configuration(
        self,
        namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        lakehouse_registration: Optional[
            "aws_sdk_redshift_serverless.types.lakehouse_registration.LakehouseRegistration"
        ] = None,
        catalog_name: Optional[
            "aws_sdk_redshift_serverless.types.catalog_name_string.CatalogNameString"
        ] = None,
        lakehouse_idc_registration: Optional[
            "aws_sdk_redshift_serverless.types.lakehouse_idc_registration.LakehouseIdcRegistration"
        ] = None,
        lakehouse_idc_application_arn: Optional[str] = None,
        dry_run: Optional[bool] = None,
    ) -> "aws_sdk_redshift_serverless.types.update_lakehouse_configuration_response.UpdateLakehouseConfigurationResponse":
        """<p>Modifies the lakehouse configuration for a namespace. This operation allows you to manage Amazon Redshift federated permissions and Amazon Web Services IAM Identity Center trusted identity propagation.</p>

        Args:
            namespace_name: <p>The name of the namespace whose lakehouse configuration you want to modify.</p>
            lakehouse_registration: <p>Specifies whether to register or deregister the namespace with Amazon Redshift federated permissions. Valid values are <code>Register</code> or <code>Deregister</code>.</p>
            catalog_name: <p>The name of the Glue Data Catalog that will be associated with the namespace enabled with Amazon Redshift federated permissions.</p> <p>Pattern: <code>^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$</code> </p>
            lakehouse_idc_registration: <p>Modifies the Amazon Web Services IAM Identity Center trusted identity propagation on a namespace enabled with Amazon Redshift federated permissions. Valid values are <code>Associate</code> or <code>Disassociate</code>.</p>
            lakehouse_idc_application_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling Amazon Web Services IAM Identity Center trusted identity propagation on a namespace enabled with Amazon Redshift federated permissions.</p>
            dry_run: <p>A boolean value that, if <code>true</code>, validates the request without actually updating the lakehouse configuration. Use this to check for errors before making changes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.update_lakehouse_configuration_request.UpdateLakehouseConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.update_lakehouse_configuration_response.UpdateLakehouseConfigurationResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.update_lakehouse_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.update_lakehouse_configuration.async_update_lakehouse_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.update_lakehouse_configuration_request.UpdateLakehouseConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["namespace_name"] = namespace_name
        if lakehouse_registration is not None:
            input_["lakehouse_registration"] = lakehouse_registration
        if catalog_name is not None:
            input_["catalog_name"] = catalog_name
        if lakehouse_idc_registration is not None:
            input_["lakehouse_idc_registration"] = lakehouse_idc_registration
        if lakehouse_idc_application_arn is not None:
            input_["lakehouse_idc_application_arn"] = lakehouse_idc_application_arn
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
