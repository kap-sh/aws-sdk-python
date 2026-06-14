from typing import TYPE_CHECKING, Optional

import aws_sdk_dsql._auth._signers
import aws_sdk_dsql._auth._sigv4
from aws_sdk_dsql._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_dsql.types.bypass_policy_lockout_safety_check
    import aws_sdk_dsql.types.client_token
    import aws_sdk_dsql.types.cluster_id
    import aws_sdk_dsql.types.cluster_summary
    import aws_sdk_dsql.types.create_cluster_input
    import aws_sdk_dsql.types.create_cluster_output
    import aws_sdk_dsql.types.delete_cluster_input
    import aws_sdk_dsql.types.delete_cluster_output
    import aws_sdk_dsql.types.delete_cluster_policy_input
    import aws_sdk_dsql.types.delete_cluster_policy_output
    import aws_sdk_dsql.types.deletion_protection_enabled
    import aws_sdk_dsql.types.get_cluster_input
    import aws_sdk_dsql.types.get_cluster_output
    import aws_sdk_dsql.types.get_cluster_policy_input
    import aws_sdk_dsql.types.get_cluster_policy_output
    import aws_sdk_dsql.types.get_vpc_endpoint_service_name_input
    import aws_sdk_dsql.types.get_vpc_endpoint_service_name_output
    import aws_sdk_dsql.types.kms_encryption_key
    import aws_sdk_dsql.types.list_clusters_input
    import aws_sdk_dsql.types.list_clusters_output
    import aws_sdk_dsql.types.max_results
    import aws_sdk_dsql.types.multi_region_properties
    import aws_sdk_dsql.types.next_token
    import aws_sdk_dsql.types.policy_document
    import aws_sdk_dsql.types.policy_version
    import aws_sdk_dsql.types.put_cluster_policy_input
    import aws_sdk_dsql.types.put_cluster_policy_output
    import aws_sdk_dsql.types.tag_map
    import aws_sdk_dsql.types.update_cluster_input
    import aws_sdk_dsql.types.update_cluster_output
    from aws_sdk_dsql._services.async_dsql import AsyncDSQLClient, AsyncDSQLClientConfig
    from aws_sdk_dsql._services.dsql import DSQLClient, DSQLClientConfig


class Cluster:
    def __init__(self, service: DSQLClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        deletion_protection_enabled: Optional[
            "aws_sdk_dsql.types.deletion_protection_enabled.DeletionProtectionEnabled"
        ] = None,
        kms_encryption_key: Optional[
            "aws_sdk_dsql.types.kms_encryption_key.KmsEncryptionKey"
        ] = None,
        tags: Optional["aws_sdk_dsql.types.tag_map.TagMap"] = None,
        client_token: Optional["aws_sdk_dsql.types.client_token.ClientToken"] = None,
        multi_region_properties: Optional[
            "aws_sdk_dsql.types.multi_region_properties.MultiRegionProperties"
        ] = None,
        policy: Optional["aws_sdk_dsql.types.policy_document.PolicyDocument"] = None,
        bypass_policy_lockout_safety_check: Optional[
            "aws_sdk_dsql.types.bypass_policy_lockout_safety_check.BypassPolicyLockoutSafetyCheck"
        ] = None,
    ) -> "aws_sdk_dsql.types.create_cluster_output.CreateClusterOutput":
        """<p>The CreateCluster API allows you to create both single-Region clusters and multi-Region clusters. With the addition of the <i>multiRegionProperties</i> parameter, you can create a cluster with witness Region support and establish peer relationships with clusters in other Regions during creation.</p> <note> <p>Creating multi-Region clusters requires additional IAM permissions beyond those needed for single-Region clusters, as detailed in the <b>Required permissions</b> section below.</p> </note> <p> <b>Required permissions</b> </p> <dl> <dt>dsql:CreateCluster</dt> <dd> <p>Required to create a cluster.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> </dd> <dt>dsql:TagResource</dt> <dd> <p>Permission to add tags to a resource.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> </dd> <dt>dsql:PutMultiRegionProperties</dt> <dd> <p>Permission to configure multi-Region properties for a cluster.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> </dd> <dt>dsql:AddPeerCluster</dt> <dd> <p>When specifying <code>multiRegionProperties.clusters</code>, permission to add peer clusters.</p> <p>Resources:</p> <ul> <li> <p>Local cluster: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> </li> <li> <p>Each peer cluster: exact ARN of each specified peer cluster</p> </li> </ul> </dd> <dt>dsql:PutWitnessRegion</dt> <dd> <p>When specifying <code>multiRegionProperties.witnessRegion</code>, permission to set a witness Region. This permission is checked both in the cluster Region and in the witness Region.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> <p>Condition Keys: <code>dsql:WitnessRegion</code> (matching the specified witness region)</p> </dd> </dl> <important> <ul> <li> <p>The witness Region specified in <code>multiRegionProperties.witnessRegion</code> cannot be the same as the cluster's Region.</p> </li> </ul> </important>

        Args:
            deletion_protection_enabled: <p>If enabled, you can't delete your cluster. You must first disable this property before you can delete your cluster.</p>
            kms_encryption_key: <p>The KMS key that encrypts and protects the data on your cluster. You can specify the ARN, ID, or alias of an existing key or have Amazon Web Services create a default key for you.</p>
            tags: <p>A map of key and value pairs to use to tag your cluster.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>
            multi_region_properties: <p>The configuration settings when creating a multi-Region cluster, including the witness region and linked cluster properties.</p>
            policy: <p>An optional resource-based policy document in JSON format that defines access permissions for the cluster.</p>
            bypass_policy_lockout_safety_check: <p>An optional field that controls whether to bypass the lockout prevention check. When set to true, this parameter allows you to apply a policy that might lock you out of the cluster. Use with caution.</p>

        Examples:
            Create Cluster

            >>> client.create(deletion_protection_enabled=False, tags={'MyKey': 'MyValue'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dsql.types.create_cluster_input.CreateClusterInput]",
        ) -> OperationResponse[
            "aws_sdk_dsql.types.create_cluster_output.CreateClusterOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.create_cluster

            output, http_response = (
                aws_sdk_dsql._operations.dsql.create_cluster.create_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.create_cluster_input.CreateClusterInput = {}  # type: ignore[typeddict-item]
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if kms_encryption_key is not None:
            input_["kms_encryption_key"] = kms_encryption_key
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token
        if multi_region_properties is not None:
            input_["multi_region_properties"] = multi_region_properties
        if policy is not None:
            input_["policy"] = policy
        if bypass_policy_lockout_safety_check is not None:
            input_["bypass_policy_lockout_safety_check"] = (
                bypass_policy_lockout_safety_check
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        identifier: "aws_sdk_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> "aws_sdk_dsql.types.get_cluster_output.GetClusterOutput":
        """<p>Retrieves information about a cluster.</p>

        Args:
            identifier: <p>The ID of the cluster to retrieve.</p>

        Examples:
            Get Cluster

            >>> client.read(identifier='kiqenqglxyl2snyvkvnj2c3s2e')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dsql.types.get_cluster_input.GetClusterInput]",
        ) -> OperationResponse[
            "aws_sdk_dsql.types.get_cluster_output.GetClusterOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.get_cluster

            output, http_response = (
                aws_sdk_dsql._operations.dsql.get_cluster.get_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.get_cluster_input.GetClusterInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        identifier: "aws_sdk_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        deletion_protection_enabled: Optional[
            "aws_sdk_dsql.types.deletion_protection_enabled.DeletionProtectionEnabled"
        ] = None,
        kms_encryption_key: Optional[
            "aws_sdk_dsql.types.kms_encryption_key.KmsEncryptionKey"
        ] = None,
        client_token: Optional["aws_sdk_dsql.types.client_token.ClientToken"] = None,
        multi_region_properties: Optional[
            "aws_sdk_dsql.types.multi_region_properties.MultiRegionProperties"
        ] = None,
    ) -> "aws_sdk_dsql.types.update_cluster_output.UpdateClusterOutput":
        """<p>The <i>UpdateCluster</i> API allows you to modify both single-Region and multi-Region cluster configurations. With the <i>multiRegionProperties</i> parameter, you can add or modify witness Region support and manage peer relationships with clusters in other Regions.</p> <note> <p>Note that updating multi-Region clusters requires additional IAM permissions beyond those needed for standard cluster updates, as detailed in the Permissions section.</p> </note> <p> <b>Required permissions</b> </p> <dl> <dt>dsql:UpdateCluster</dt> <dd> <p>Permission to update a DSQL cluster.</p> <p>Resources: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> </dd> </dl> <dl> <dt>dsql:PutMultiRegionProperties</dt> <dd> <p>Permission to configure multi-Region properties for a cluster.</p> <p>Resources: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> </dd> </dl> <dl> <dt>dsql:GetCluster</dt> <dd> <p>Permission to retrieve cluster information.</p> <p>Resources: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> </dd> <dt>dsql:AddPeerCluster</dt> <dd> <p>Permission to add peer clusters.</p> <p>Resources:</p> <ul> <li> <p>Local cluster: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> </li> <li> <p>Each peer cluster: exact ARN of each specified peer cluster</p> </li> </ul> </dd> <dt>dsql:RemovePeerCluster</dt> <dd> <p>Permission to remove peer clusters. The <i>dsql:RemovePeerCluster</i> permission uses a wildcard ARN pattern to simplify permission management during updates.</p> <p>Resources: <code>arn:aws:dsql:*:<i>account-id</i>:cluster/*</code> </p> </dd> </dl> <dl> <dt>dsql:PutWitnessRegion</dt> <dd> <p>Permission to set a witness Region.</p> <p>Resources: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> <p>Condition Keys: dsql:WitnessRegion (matching the specified witness Region)</p> <p> <b>This permission is checked both in the cluster Region and in the witness Region.</b> </p> </dd> </dl> <important> <ul> <li> <p>The witness region specified in <code>multiRegionProperties.witnessRegion</code> cannot be the same as the cluster's Region.</p> </li> <li> <p>When updating clusters with peer relationships, permissions are checked for both adding and removing peers.</p> </li> <li> <p>The <code>dsql:RemovePeerCluster</code> permission uses a wildcard ARN pattern to simplify permission management during updates.</p> </li> </ul> </important>

        Args:
            identifier: <p>The ID of the cluster you want to update.</p>
            deletion_protection_enabled: <p>Specifies whether to enable deletion protection in your cluster.</p>
            kms_encryption_key: <p>The KMS key that encrypts and protects the data on your cluster. You can specify the ARN, ID, or alias of an existing key or have Amazon Web Services create a default key for you.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully. The subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>
            multi_region_properties: <p>The new multi-Region cluster configuration settings to be applied during an update operation.</p>

        Examples:
            Update Cluster

            >>> client.update(identifier='kiqenqglxyl2snyvkvnj2c3s2e', deletion_protection_enabled=False)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dsql.types.update_cluster_input.UpdateClusterInput]",
        ) -> OperationResponse[
            "aws_sdk_dsql.types.update_cluster_output.UpdateClusterOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.update_cluster

            output, http_response = (
                aws_sdk_dsql._operations.dsql.update_cluster.update_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.update_cluster_input.UpdateClusterInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if kms_encryption_key is not None:
            input_["kms_encryption_key"] = kms_encryption_key
        if client_token is not None:
            input_["client_token"] = client_token
        if multi_region_properties is not None:
            input_["multi_region_properties"] = multi_region_properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        identifier: "aws_sdk_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        client_token: Optional["aws_sdk_dsql.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_dsql.types.delete_cluster_output.DeleteClusterOutput":
        """<p>Deletes a cluster in Amazon Aurora DSQL.</p>

        Args:
            identifier: <p>The ID of the cluster to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully. The subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>

        Examples:
            Delete Cluster

            >>> client.delete(identifier='kiqenqglxyl2snyvkvnj2c3s2e')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dsql.types.delete_cluster_input.DeleteClusterInput]",
        ) -> OperationResponse[
            "aws_sdk_dsql.types.delete_cluster_output.DeleteClusterOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.delete_cluster

            output, http_response = (
                aws_sdk_dsql._operations.dsql.delete_cluster.delete_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.delete_cluster_input.DeleteClusterInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        max_results: Optional["aws_sdk_dsql.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_dsql.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_dsql.types.list_clusters_output.ListClustersOutput":
        """<p>Retrieves information about a list of clusters.</p>

        Args:
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.</p>
            next_token: <p>If your initial ListClusters operation returns a nextToken, you can include the returned nextToken in following ListClusters operations, which returns results in the next page.</p>

        Examples:
            List Clusters

            >>> client.list(max_results=20)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dsql.types.list_clusters_input.ListClustersInput]",
        ) -> OperationResponse[
            "aws_sdk_dsql.types.list_clusters_output.ListClustersOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.list_clusters

            output, http_response = (
                aws_sdk_dsql._operations.dsql.list_clusters.list_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.list_clusters_input.ListClustersInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_cluster_policy(
        self,
        identifier: "aws_sdk_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        expected_policy_version: Optional[
            "aws_sdk_dsql.types.policy_version.PolicyVersion"
        ] = None,
        client_token: Optional["aws_sdk_dsql.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_dsql.types.delete_cluster_policy_output.DeleteClusterPolicyOutput":
        """<p>Deletes the resource-based policy attached to a cluster. This removes all access permissions defined by the policy, reverting to default access controls.</p>

        Args:
            expected_policy_version: <p>The expected version of the policy to delete. This parameter ensures that you're deleting the correct version of the policy and helps prevent accidental deletions.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dsql.types.delete_cluster_policy_input.DeleteClusterPolicyInput]",
        ) -> OperationResponse[
            "aws_sdk_dsql.types.delete_cluster_policy_output.DeleteClusterPolicyOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.delete_cluster_policy

            output, http_response = (
                aws_sdk_dsql._operations.dsql.delete_cluster_policy.delete_cluster_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.delete_cluster_policy_input.DeleteClusterPolicyInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if expected_policy_version is not None:
            input_["expected_policy_version"] = expected_policy_version
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_cluster_policy(
        self,
        identifier: "aws_sdk_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> "aws_sdk_dsql.types.get_cluster_policy_output.GetClusterPolicyOutput":
        """<p>Retrieves the resource-based policy document attached to a cluster. This policy defines the access permissions and conditions for the cluster.</p>

        Args:
            identifier: <p>The ID of the cluster to retrieve the policy from.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dsql.types.get_cluster_policy_input.GetClusterPolicyInput]",
        ) -> OperationResponse[
            "aws_sdk_dsql.types.get_cluster_policy_output.GetClusterPolicyOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.get_cluster_policy

            output, http_response = (
                aws_sdk_dsql._operations.dsql.get_cluster_policy.get_cluster_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.get_cluster_policy_input.GetClusterPolicyInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_vpc_endpoint_service_name(
        self,
        identifier: "aws_sdk_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> "aws_sdk_dsql.types.get_vpc_endpoint_service_name_output.GetVpcEndpointServiceNameOutput":
        """<p>Retrieves the VPC endpoint service name.</p>

        Args:
            identifier: <p>The ID of the cluster to retrieve.</p>

        Examples:
            Get VPC Endpoint Service Name

            >>> client.get_vpc_endpoint_service_name(identifier='kiqenqglxyl2snyvkvnj2c3s2e')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dsql.types.get_vpc_endpoint_service_name_input.GetVpcEndpointServiceNameInput]",
        ) -> OperationResponse[
            "aws_sdk_dsql.types.get_vpc_endpoint_service_name_output.GetVpcEndpointServiceNameOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.get_vpc_endpoint_service_name

            output, http_response = (
                aws_sdk_dsql._operations.dsql.get_vpc_endpoint_service_name.get_vpc_endpoint_service_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.get_vpc_endpoint_service_name_input.GetVpcEndpointServiceNameInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_cluster_policy(
        self,
        identifier: "aws_sdk_dsql.types.cluster_id.ClusterId",
        policy: "aws_sdk_dsql.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        bypass_policy_lockout_safety_check: Optional[
            "aws_sdk_dsql.types.bypass_policy_lockout_safety_check.BypassPolicyLockoutSafetyCheck"
        ] = None,
        expected_policy_version: Optional[
            "aws_sdk_dsql.types.policy_version.PolicyVersion"
        ] = None,
        client_token: Optional["aws_sdk_dsql.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_dsql.types.put_cluster_policy_output.PutClusterPolicyOutput":
        """<p>Attaches a resource-based policy to a cluster. This policy defines access permissions and conditions for the cluster, allowing you to control which principals can perform actions on the cluster.</p>

        Args:
            policy: <p>The resource-based policy document to attach to the cluster. This should be a valid JSON policy document that defines permissions and conditions.</p>
            bypass_policy_lockout_safety_check: <p>A flag that allows you to bypass the policy lockout safety check. When set to true, this parameter allows you to apply a policy that might lock you out of the cluster. Use with caution.</p>
            expected_policy_version: <p>The expected version of the current policy. This parameter ensures that you're updating the correct version of the policy and helps prevent concurrent modification conflicts.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dsql.types.put_cluster_policy_input.PutClusterPolicyInput]",
        ) -> OperationResponse[
            "aws_sdk_dsql.types.put_cluster_policy_output.PutClusterPolicyOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.put_cluster_policy

            output, http_response = (
                aws_sdk_dsql._operations.dsql.put_cluster_policy.put_cluster_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.put_cluster_policy_input.PutClusterPolicyInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        input_["policy"] = policy
        if bypass_policy_lockout_safety_check is not None:
            input_["bypass_policy_lockout_safety_check"] = (
                bypass_policy_lockout_safety_check
            )
        if expected_policy_version is not None:
            input_["expected_policy_version"] = expected_policy_version
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncCluster:
    def __init__(self, service: AsyncDSQLClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
        deletion_protection_enabled: Optional[
            "aws_sdk_dsql.types.deletion_protection_enabled.DeletionProtectionEnabled"
        ] = None,
        kms_encryption_key: Optional[
            "aws_sdk_dsql.types.kms_encryption_key.KmsEncryptionKey"
        ] = None,
        tags: Optional["aws_sdk_dsql.types.tag_map.TagMap"] = None,
        client_token: Optional["aws_sdk_dsql.types.client_token.ClientToken"] = None,
        multi_region_properties: Optional[
            "aws_sdk_dsql.types.multi_region_properties.MultiRegionProperties"
        ] = None,
        policy: Optional["aws_sdk_dsql.types.policy_document.PolicyDocument"] = None,
        bypass_policy_lockout_safety_check: Optional[
            "aws_sdk_dsql.types.bypass_policy_lockout_safety_check.BypassPolicyLockoutSafetyCheck"
        ] = None,
    ) -> "aws_sdk_dsql.types.create_cluster_output.CreateClusterOutput":
        """<p>The CreateCluster API allows you to create both single-Region clusters and multi-Region clusters. With the addition of the <i>multiRegionProperties</i> parameter, you can create a cluster with witness Region support and establish peer relationships with clusters in other Regions during creation.</p> <note> <p>Creating multi-Region clusters requires additional IAM permissions beyond those needed for single-Region clusters, as detailed in the <b>Required permissions</b> section below.</p> </note> <p> <b>Required permissions</b> </p> <dl> <dt>dsql:CreateCluster</dt> <dd> <p>Required to create a cluster.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> </dd> <dt>dsql:TagResource</dt> <dd> <p>Permission to add tags to a resource.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> </dd> <dt>dsql:PutMultiRegionProperties</dt> <dd> <p>Permission to configure multi-Region properties for a cluster.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> </dd> <dt>dsql:AddPeerCluster</dt> <dd> <p>When specifying <code>multiRegionProperties.clusters</code>, permission to add peer clusters.</p> <p>Resources:</p> <ul> <li> <p>Local cluster: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> </li> <li> <p>Each peer cluster: exact ARN of each specified peer cluster</p> </li> </ul> </dd> <dt>dsql:PutWitnessRegion</dt> <dd> <p>When specifying <code>multiRegionProperties.witnessRegion</code>, permission to set a witness Region. This permission is checked both in the cluster Region and in the witness Region.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> <p>Condition Keys: <code>dsql:WitnessRegion</code> (matching the specified witness region)</p> </dd> </dl> <important> <ul> <li> <p>The witness Region specified in <code>multiRegionProperties.witnessRegion</code> cannot be the same as the cluster's Region.</p> </li> </ul> </important>

        Args:
            deletion_protection_enabled: <p>If enabled, you can't delete your cluster. You must first disable this property before you can delete your cluster.</p>
            kms_encryption_key: <p>The KMS key that encrypts and protects the data on your cluster. You can specify the ARN, ID, or alias of an existing key or have Amazon Web Services create a default key for you.</p>
            tags: <p>A map of key and value pairs to use to tag your cluster.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>
            multi_region_properties: <p>The configuration settings when creating a multi-Region cluster, including the witness region and linked cluster properties.</p>
            policy: <p>An optional resource-based policy document in JSON format that defines access permissions for the cluster.</p>
            bypass_policy_lockout_safety_check: <p>An optional field that controls whether to bypass the lockout prevention check. When set to true, this parameter allows you to apply a policy that might lock you out of the cluster. Use with caution.</p>

        Examples:
            Create Cluster

            >>> await client.create(deletion_protection_enabled=False, tags={'MyKey': 'MyValue'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dsql.types.create_cluster_input.CreateClusterInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_dsql.types.create_cluster_output.CreateClusterOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.create_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_dsql._operations.dsql.create_cluster.async_create_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.create_cluster_input.CreateClusterInput = {}  # type: ignore[typeddict-item]
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if kms_encryption_key is not None:
            input_["kms_encryption_key"] = kms_encryption_key
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token
        if multi_region_properties is not None:
            input_["multi_region_properties"] = multi_region_properties
        if policy is not None:
            input_["policy"] = policy
        if bypass_policy_lockout_safety_check is not None:
            input_["bypass_policy_lockout_safety_check"] = (
                bypass_policy_lockout_safety_check
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        identifier: "aws_sdk_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
    ) -> "aws_sdk_dsql.types.get_cluster_output.GetClusterOutput":
        """<p>Retrieves information about a cluster.</p>

        Args:
            identifier: <p>The ID of the cluster to retrieve.</p>

        Examples:
            Get Cluster

            >>> await client.read(identifier='kiqenqglxyl2snyvkvnj2c3s2e')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dsql.types.get_cluster_input.GetClusterInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_dsql.types.get_cluster_output.GetClusterOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.get_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_dsql._operations.dsql.get_cluster.async_get_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.get_cluster_input.GetClusterInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        identifier: "aws_sdk_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
        deletion_protection_enabled: Optional[
            "aws_sdk_dsql.types.deletion_protection_enabled.DeletionProtectionEnabled"
        ] = None,
        kms_encryption_key: Optional[
            "aws_sdk_dsql.types.kms_encryption_key.KmsEncryptionKey"
        ] = None,
        client_token: Optional["aws_sdk_dsql.types.client_token.ClientToken"] = None,
        multi_region_properties: Optional[
            "aws_sdk_dsql.types.multi_region_properties.MultiRegionProperties"
        ] = None,
    ) -> "aws_sdk_dsql.types.update_cluster_output.UpdateClusterOutput":
        """<p>The <i>UpdateCluster</i> API allows you to modify both single-Region and multi-Region cluster configurations. With the <i>multiRegionProperties</i> parameter, you can add or modify witness Region support and manage peer relationships with clusters in other Regions.</p> <note> <p>Note that updating multi-Region clusters requires additional IAM permissions beyond those needed for standard cluster updates, as detailed in the Permissions section.</p> </note> <p> <b>Required permissions</b> </p> <dl> <dt>dsql:UpdateCluster</dt> <dd> <p>Permission to update a DSQL cluster.</p> <p>Resources: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> </dd> </dl> <dl> <dt>dsql:PutMultiRegionProperties</dt> <dd> <p>Permission to configure multi-Region properties for a cluster.</p> <p>Resources: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> </dd> </dl> <dl> <dt>dsql:GetCluster</dt> <dd> <p>Permission to retrieve cluster information.</p> <p>Resources: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> </dd> <dt>dsql:AddPeerCluster</dt> <dd> <p>Permission to add peer clusters.</p> <p>Resources:</p> <ul> <li> <p>Local cluster: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> </li> <li> <p>Each peer cluster: exact ARN of each specified peer cluster</p> </li> </ul> </dd> <dt>dsql:RemovePeerCluster</dt> <dd> <p>Permission to remove peer clusters. The <i>dsql:RemovePeerCluster</i> permission uses a wildcard ARN pattern to simplify permission management during updates.</p> <p>Resources: <code>arn:aws:dsql:*:<i>account-id</i>:cluster/*</code> </p> </dd> </dl> <dl> <dt>dsql:PutWitnessRegion</dt> <dd> <p>Permission to set a witness Region.</p> <p>Resources: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> <p>Condition Keys: dsql:WitnessRegion (matching the specified witness Region)</p> <p> <b>This permission is checked both in the cluster Region and in the witness Region.</b> </p> </dd> </dl> <important> <ul> <li> <p>The witness region specified in <code>multiRegionProperties.witnessRegion</code> cannot be the same as the cluster's Region.</p> </li> <li> <p>When updating clusters with peer relationships, permissions are checked for both adding and removing peers.</p> </li> <li> <p>The <code>dsql:RemovePeerCluster</code> permission uses a wildcard ARN pattern to simplify permission management during updates.</p> </li> </ul> </important>

        Args:
            identifier: <p>The ID of the cluster you want to update.</p>
            deletion_protection_enabled: <p>Specifies whether to enable deletion protection in your cluster.</p>
            kms_encryption_key: <p>The KMS key that encrypts and protects the data on your cluster. You can specify the ARN, ID, or alias of an existing key or have Amazon Web Services create a default key for you.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully. The subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>
            multi_region_properties: <p>The new multi-Region cluster configuration settings to be applied during an update operation.</p>

        Examples:
            Update Cluster

            >>> await client.update(identifier='kiqenqglxyl2snyvkvnj2c3s2e', deletion_protection_enabled=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dsql.types.update_cluster_input.UpdateClusterInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_dsql.types.update_cluster_output.UpdateClusterOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.update_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_dsql._operations.dsql.update_cluster.async_update_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.update_cluster_input.UpdateClusterInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if kms_encryption_key is not None:
            input_["kms_encryption_key"] = kms_encryption_key
        if client_token is not None:
            input_["client_token"] = client_token
        if multi_region_properties is not None:
            input_["multi_region_properties"] = multi_region_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        identifier: "aws_sdk_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
        client_token: Optional["aws_sdk_dsql.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_dsql.types.delete_cluster_output.DeleteClusterOutput":
        """<p>Deletes a cluster in Amazon Aurora DSQL.</p>

        Args:
            identifier: <p>The ID of the cluster to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully. The subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>

        Examples:
            Delete Cluster

            >>> await client.delete(identifier='kiqenqglxyl2snyvkvnj2c3s2e')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dsql.types.delete_cluster_input.DeleteClusterInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_dsql.types.delete_cluster_output.DeleteClusterOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.delete_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_dsql._operations.dsql.delete_cluster.async_delete_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.delete_cluster_input.DeleteClusterInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
        max_results: Optional["aws_sdk_dsql.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_dsql.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_dsql.types.list_clusters_output.ListClustersOutput":
        """<p>Retrieves information about a list of clusters.</p>

        Args:
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.</p>
            next_token: <p>If your initial ListClusters operation returns a nextToken, you can include the returned nextToken in following ListClusters operations, which returns results in the next page.</p>

        Examples:
            List Clusters

            >>> await client.list(max_results=20)
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dsql.types.list_clusters_input.ListClustersInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_dsql.types.list_clusters_output.ListClustersOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.list_clusters

            (
                output,
                http_response,
            ) = await aws_sdk_dsql._operations.dsql.list_clusters.async_list_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.list_clusters_input.ListClustersInput = {}  # type: ignore[typeddict-item]
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

    async def delete_cluster_policy(
        self,
        identifier: "aws_sdk_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
        expected_policy_version: Optional[
            "aws_sdk_dsql.types.policy_version.PolicyVersion"
        ] = None,
        client_token: Optional["aws_sdk_dsql.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_dsql.types.delete_cluster_policy_output.DeleteClusterPolicyOutput":
        """<p>Deletes the resource-based policy attached to a cluster. This removes all access permissions defined by the policy, reverting to default access controls.</p>

        Args:
            expected_policy_version: <p>The expected version of the policy to delete. This parameter ensures that you're deleting the correct version of the policy and helps prevent accidental deletions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dsql.types.delete_cluster_policy_input.DeleteClusterPolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_dsql.types.delete_cluster_policy_output.DeleteClusterPolicyOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.delete_cluster_policy

            (
                output,
                http_response,
            ) = await aws_sdk_dsql._operations.dsql.delete_cluster_policy.async_delete_cluster_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.delete_cluster_policy_input.DeleteClusterPolicyInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if expected_policy_version is not None:
            input_["expected_policy_version"] = expected_policy_version
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_cluster_policy(
        self,
        identifier: "aws_sdk_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
    ) -> "aws_sdk_dsql.types.get_cluster_policy_output.GetClusterPolicyOutput":
        """<p>Retrieves the resource-based policy document attached to a cluster. This policy defines the access permissions and conditions for the cluster.</p>

        Args:
            identifier: <p>The ID of the cluster to retrieve the policy from.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dsql.types.get_cluster_policy_input.GetClusterPolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_dsql.types.get_cluster_policy_output.GetClusterPolicyOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.get_cluster_policy

            (
                output,
                http_response,
            ) = await aws_sdk_dsql._operations.dsql.get_cluster_policy.async_get_cluster_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.get_cluster_policy_input.GetClusterPolicyInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_vpc_endpoint_service_name(
        self,
        identifier: "aws_sdk_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
    ) -> "aws_sdk_dsql.types.get_vpc_endpoint_service_name_output.GetVpcEndpointServiceNameOutput":
        """<p>Retrieves the VPC endpoint service name.</p>

        Args:
            identifier: <p>The ID of the cluster to retrieve.</p>

        Examples:
            Get VPC Endpoint Service Name

            >>> await client.get_vpc_endpoint_service_name(identifier='kiqenqglxyl2snyvkvnj2c3s2e')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dsql.types.get_vpc_endpoint_service_name_input.GetVpcEndpointServiceNameInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_dsql.types.get_vpc_endpoint_service_name_output.GetVpcEndpointServiceNameOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.get_vpc_endpoint_service_name

            (
                output,
                http_response,
            ) = await aws_sdk_dsql._operations.dsql.get_vpc_endpoint_service_name.async_get_vpc_endpoint_service_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.get_vpc_endpoint_service_name_input.GetVpcEndpointServiceNameInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_cluster_policy(
        self,
        identifier: "aws_sdk_dsql.types.cluster_id.ClusterId",
        policy: "aws_sdk_dsql.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
        bypass_policy_lockout_safety_check: Optional[
            "aws_sdk_dsql.types.bypass_policy_lockout_safety_check.BypassPolicyLockoutSafetyCheck"
        ] = None,
        expected_policy_version: Optional[
            "aws_sdk_dsql.types.policy_version.PolicyVersion"
        ] = None,
        client_token: Optional["aws_sdk_dsql.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_dsql.types.put_cluster_policy_output.PutClusterPolicyOutput":
        """<p>Attaches a resource-based policy to a cluster. This policy defines access permissions and conditions for the cluster, allowing you to control which principals can perform actions on the cluster.</p>

        Args:
            policy: <p>The resource-based policy document to attach to the cluster. This should be a valid JSON policy document that defines permissions and conditions.</p>
            bypass_policy_lockout_safety_check: <p>A flag that allows you to bypass the policy lockout safety check. When set to true, this parameter allows you to apply a policy that might lock you out of the cluster. Use with caution.</p>
            expected_policy_version: <p>The expected version of the current policy. This parameter ensures that you're updating the correct version of the policy and helps prevent concurrent modification conflicts.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dsql.types.put_cluster_policy_input.PutClusterPolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_dsql.types.put_cluster_policy_output.PutClusterPolicyOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.put_cluster_policy

            (
                output,
                http_response,
            ) = await aws_sdk_dsql._operations.dsql.put_cluster_policy.async_put_cluster_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.put_cluster_policy_input.PutClusterPolicyInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        input_["policy"] = policy
        if bypass_policy_lockout_safety_check is not None:
            input_["bypass_policy_lockout_safety_check"] = (
                bypass_policy_lockout_safety_check
            )
        if expected_policy_version is not None:
            input_["expected_policy_version"] = expected_policy_version
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
