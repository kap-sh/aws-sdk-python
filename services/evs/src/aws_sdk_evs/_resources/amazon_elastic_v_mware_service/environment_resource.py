from typing import TYPE_CHECKING, Optional

from aws_sdk_evs._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_evs.types.allocation_id
    import aws_sdk_evs.types.appliance_fqdn
    import aws_sdk_evs.types.associate_eip_to_vlan_request
    import aws_sdk_evs.types.associate_eip_to_vlan_response
    import aws_sdk_evs.types.association_id
    import aws_sdk_evs.types.client_token
    import aws_sdk_evs.types.connectivity_info
    import aws_sdk_evs.types.connector
    import aws_sdk_evs.types.connector_id
    import aws_sdk_evs.types.connector_type
    import aws_sdk_evs.types.create_entitlement_request
    import aws_sdk_evs.types.create_entitlement_response
    import aws_sdk_evs.types.create_environment_connector_request
    import aws_sdk_evs.types.create_environment_connector_response
    import aws_sdk_evs.types.create_environment_host_request
    import aws_sdk_evs.types.create_environment_host_response
    import aws_sdk_evs.types.create_environment_request
    import aws_sdk_evs.types.create_environment_response
    import aws_sdk_evs.types.delete_entitlement_request
    import aws_sdk_evs.types.delete_entitlement_response
    import aws_sdk_evs.types.delete_environment_connector_request
    import aws_sdk_evs.types.delete_environment_connector_response
    import aws_sdk_evs.types.delete_environment_host_request
    import aws_sdk_evs.types.delete_environment_host_response
    import aws_sdk_evs.types.delete_environment_request
    import aws_sdk_evs.types.delete_environment_response
    import aws_sdk_evs.types.disassociate_eip_from_vlan_request
    import aws_sdk_evs.types.disassociate_eip_from_vlan_response
    import aws_sdk_evs.types.entitlement_type
    import aws_sdk_evs.types.environment_id
    import aws_sdk_evs.types.environment_name
    import aws_sdk_evs.types.environment_state_list
    import aws_sdk_evs.types.environment_summary
    import aws_sdk_evs.types.esx_version
    import aws_sdk_evs.types.get_depot_url_request
    import aws_sdk_evs.types.get_depot_url_response
    import aws_sdk_evs.types.get_environment_request
    import aws_sdk_evs.types.get_environment_response
    import aws_sdk_evs.types.host
    import aws_sdk_evs.types.host_info_for_create
    import aws_sdk_evs.types.host_info_for_create_list
    import aws_sdk_evs.types.host_name
    import aws_sdk_evs.types.initial_vlans
    import aws_sdk_evs.types.license_info_list
    import aws_sdk_evs.types.list_environment_connectors_request
    import aws_sdk_evs.types.list_environment_connectors_response
    import aws_sdk_evs.types.list_environment_hosts_request
    import aws_sdk_evs.types.list_environment_hosts_response
    import aws_sdk_evs.types.list_environment_vlans_request
    import aws_sdk_evs.types.list_environment_vlans_response
    import aws_sdk_evs.types.list_environments_request
    import aws_sdk_evs.types.list_environments_response
    import aws_sdk_evs.types.list_vm_entitlements_request
    import aws_sdk_evs.types.list_vm_entitlements_response
    import aws_sdk_evs.types.max_results
    import aws_sdk_evs.types.pagination_token
    import aws_sdk_evs.types.request_tag_map
    import aws_sdk_evs.types.secret_identifier
    import aws_sdk_evs.types.service_access_security_groups
    import aws_sdk_evs.types.subnet_id
    import aws_sdk_evs.types.update_environment_connector_request
    import aws_sdk_evs.types.update_environment_connector_response
    import aws_sdk_evs.types.vcf_hostnames
    import aws_sdk_evs.types.vcf_version
    import aws_sdk_evs.types.vlan
    import aws_sdk_evs.types.vm_entitlement
    import aws_sdk_evs.types.vm_id_list
    import aws_sdk_evs.types.vpc_id
    from aws_sdk_evs._services.async_evs import AsyncevsClient, AsyncevsClientConfig
    from aws_sdk_evs._services.evs import evsClient, evsClientConfig


class EnvironmentResource:
    def __init__(self, service: evsClient) -> None:
        self._service = service

    def create(
        self,
        vpc_id: "aws_sdk_evs.types.vpc_id.VpcId",
        service_access_subnet_id: "aws_sdk_evs.types.subnet_id.SubnetId",
        vcf_version: "aws_sdk_evs.types.vcf_version.VcfVersion",
        terms_accepted: bool,
        license_info: "aws_sdk_evs.types.license_info_list.LicenseInfoList",
        initial_vlans: "aws_sdk_evs.types.initial_vlans.InitialVlans",
        hosts: "aws_sdk_evs.types.host_info_for_create_list.HostInfoForCreateList",
        connectivity_info: "aws_sdk_evs.types.connectivity_info.ConnectivityInfo",
        vcf_hostnames: "aws_sdk_evs.types.vcf_hostnames.VcfHostnames",
        site_id: str,
        *,
        config_overrides: Optional[evsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
        environment_name: Optional[
            "aws_sdk_evs.types.environment_name.EnvironmentName"
        ] = None,
        kms_key_id: Optional[str] = None,
        tags: Optional["aws_sdk_evs.types.request_tag_map.RequestTagMap"] = None,
        service_access_security_groups: Optional[
            "aws_sdk_evs.types.service_access_security_groups.ServiceAccessSecurityGroups"
        ] = None,
    ) -> "aws_sdk_evs.types.create_environment_response.CreateEnvironmentResponse":
        """<p>Creates an Amazon EVS environment that runs VCF software, such as SDDC Manager, NSX Manager, and vCenter Server.</p> <p>During environment creation, Amazon EVS performs validations on DNS settings, provisions VLAN subnets and hosts, and deploys the supplied version of VCF.</p> <p>It can take several hours to create an environment. After the deployment completes, you can configure VCF in the vSphere user interface according to your needs.</p> <important> <p>When creating a new environment, the default ESX version for the selected VCF version will be used, you cannot choose a specific ESX version in <code>CreateEnvironment</code> action. When a host has been added with a specific ESX version, it can only be upgraded using vCenter Lifecycle Manager.</p> </important> <note> <p>You cannot use the <code>dedicatedHostId</code> and <code>placementGroupId</code> parameters together in the same <code>CreateEnvironment</code> action. This results in a <code>ValidationException</code> response.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_name: <p>The name to give to your environment. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphanumeric character, and can't be longer than 100 characters. The name must be unique within the Amazon Web Services Region and Amazon Web Services account that you're creating the environment in.</p>
            kms_key_id: <p>A unique ID for the customer-managed KMS key that is used to encrypt the VCF credential pairs for SDDC Manager, NSX Manager, and vCenter appliances. These credentials are stored in Amazon Web Services Secrets Manager.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>
            service_access_security_groups: <p>The security group that controls communication between the Amazon EVS control plane and VPC. The default security group is used if a custom security group isn't specified.</p> <p>The security group should allow access to the following.</p> <ul> <li> <p>TCP/UDP access to the DNS servers</p> </li> <li> <p>HTTPS/SSH access to the host management VLAN subnet</p> </li> <li> <p>HTTPS/SSH access to the Management VM VLAN subnet</p> </li> </ul> <p>You should avoid modifying the security group rules after deployment, as this can break the persistent connection between the Amazon EVS control plane and VPC. This can cause future environment actions like adding or removing hosts to fail.</p>
            vpc_id: <p>A unique ID for the VPC that the environment is deployed inside.</p> <p>Amazon EVS requires that all VPC subnets exist in a single Availability Zone in a Region where the service is available.</p> <p>The VPC that you specify must have a valid DHCP option set with domain name, at least two DNS servers, and an NTP server. These settings are used to configure your VCF appliances and hosts. The VPC cannot be used with any other deployed Amazon EVS environment. Amazon EVS does not provide multi-VPC support for environments at this time.</p> <p>Amazon EVS does not support the following Amazon Web Services networking options for NSX overlay connectivity: cross-Region VPC peering, Amazon S3 gateway endpoints, or Amazon Web Services Direct Connect virtual private gateway associations.</p> <note> <p>Ensure that you specify a VPC that is adequately sized to accommodate the Amazon EVS subnets.</p> </note>
            service_access_subnet_id: <p>The subnet that is used to establish connectivity between the Amazon EVS control plane and VPC. Amazon EVS uses this subnet to validate mandatory DNS records for your VCF appliances and hosts and create the environment.</p>
            vcf_version: <p> The VCF version to use for the environment.</p>
            terms_accepted: <p>Customer confirmation that the customer has purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment. Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance. Amazon EVS does not validate license keys. To validate license keys, visit the Broadcom support portal.</p>
            license_info: <p>The license information that Amazon EVS requires to create an environment. Amazon EVS requires two license keys: a VCF solution key and a vSAN license key. The VCF solution key must meet minimum core requirements, and the vSAN license key must meet minimum capacity requirements for your selected instance type.</p> <p>For information about minimum license requirements, see <a href=\"https://docs.aws.amazon.com/evs/latest/userguide/vcf-license-mgmt.html\">the VCF subscriptions section</a> in the <i>Amazon EVS User Guide</i>.</p> <p>VCF licenses can be used for only one Amazon EVS environment. Amazon EVS does not support reuse of VCF licenses for multiple environments.</p> <p>VCF license information can be retrieved from the Broadcom portal.</p>
            initial_vlans: <p>The initial VLAN subnets for the Amazon EVS environment.</p> <note> <p>For each Amazon EVS VLAN subnet, you must specify a non-overlapping CIDR block. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24.</p> </note>
            hosts: <p>The ESX hosts to add to the environment. Amazon EVS requires that you provide details for a minimum of 4 hosts during environment creation.</p> <p>For each host, you must provide the desired hostname, EC2 SSH keypair name, and EC2 instance type. Optionally, you can also provide a partition or cluster placement group to use, or use Amazon EC2 Dedicated Hosts.</p>
            connectivity_info: <p> The connectivity configuration for the environment. Amazon EVS requires that you specify two route server peer IDs. During environment creation, the route server endpoints peer with the NSX edges over the NSX uplink subnet, providing BGP-based dynamic routing for overlay networks.</p>
            vcf_hostnames: <p>The DNS hostnames for the virtual machines that host the VCF management appliances. Amazon EVS requires that you provide DNS hostnames for the following appliances: vCenter, NSX Manager, SDDC Manager, and Cloud Builder.</p>
            site_id: <p>The Broadcom Site ID that is allocated to you as part of your electronic software delivery. This ID allows customer access to the Broadcom portal, and is provided to you by Broadcom at the close of your software contract or contract renewal. Amazon EVS uses the Broadcom Site ID that you provide to meet Broadcom VCF license usage reporting requirements for Amazon EVS.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.create_environment_request.CreateEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.create_environment_response.CreateEnvironmentResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_environment

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_environment.create_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.create_environment_request.CreateEnvironmentRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        if environment_name is not None:
            input["environment_name"] = environment_name
        if kms_key_id is not None:
            input["kms_key_id"] = kms_key_id
        if tags is not None:
            input["tags"] = tags
        if service_access_security_groups is not None:
            input["service_access_security_groups"] = service_access_security_groups
        input["vpc_id"] = vpc_id
        input["service_access_subnet_id"] = service_access_subnet_id
        input["vcf_version"] = vcf_version
        input["terms_accepted"] = terms_accepted
        input["license_info"] = license_info
        input["initial_vlans"] = initial_vlans
        input["hosts"] = hosts
        input["connectivity_info"] = connectivity_info
        input["vcf_hostnames"] = vcf_hostnames
        input["site_id"] = site_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[evsClientConfig] = None,
    ) -> "aws_sdk_evs.types.get_environment_response.GetEnvironmentResponse":
        """<p>Returns a description of the specified environment.</p>

        Args:
            environment_id: <p>A unique ID for the environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.get_environment_request.GetEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.get_environment_response.GetEnvironmentResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.get_environment

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.get_environment.get_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.get_environment_request.GetEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.delete_environment_response.DeleteEnvironmentResponse":
        """<p>Deletes an Amazon EVS environment.</p> <p>Amazon EVS environments will only be enabled for deletion once the hosts are deleted. You can delete hosts using the <code>DeleteEnvironmentHost</code> action.</p> <p>Environment deletion also deletes the associated Amazon EVS VLAN subnets and Amazon Web Services Secrets Manager secrets that Amazon EVS created. Amazon Web Services resources that you create are not deleted. These resources may continue to incur costs.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID associated with the environment to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.delete_environment_request.DeleteEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.delete_environment_response.DeleteEnvironmentResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_environment

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_environment.delete_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.delete_environment_request.DeleteEnvironmentRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[evsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_evs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_evs.types.max_results.MaxResults"] = None,
        state: Optional[
            "aws_sdk_evs.types.environment_state_list.EnvironmentStateList"
        ] = None,
    ) -> "aws_sdk_evs.types.list_environments_response.ListEnvironmentsResponse":
        """<p>Lists the Amazon EVS environments in your Amazon Web Services account in the specified Amazon Web Services Region.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            state: <p>The state of an environment. Used to filter response results to return only environments with the specified <code>environmentState</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.list_environments_response.ListEnvironmentsResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environments

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environments.list_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.list_environments_request.ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if state is not None:
            input["state"] = state

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_eip_to_vlan(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        vlan_name: str,
        allocation_id: "aws_sdk_evs.types.allocation_id.AllocationId",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.associate_eip_to_vlan_response.AssociateEipToVlanResponse":
        """<p>Associates an Elastic IP address with a public HCX VLAN. This operation is only allowed for public HCX VLANs at this time.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment containing the VLAN that the Elastic IP address associates with.</p>
            vlan_name: <p>The name of the VLAN. <code>hcx</code> is the only accepted VLAN name at this time.</p>
            allocation_id: <p>The Elastic IP address allocation ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.associate_eip_to_vlan_request.AssociateEipToVlanRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.associate_eip_to_vlan_response.AssociateEipToVlanResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.associate_eip_to_vlan

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.associate_eip_to_vlan.associate_eip_to_vlan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.associate_eip_to_vlan_request.AssociateEipToVlanRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["vlan_name"] = vlan_name
        input["allocation_id"] = allocation_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_entitlement(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        connector_id: "aws_sdk_evs.types.connector_id.ConnectorId",
        entitlement_type: "aws_sdk_evs.types.entitlement_type.EntitlementType",
        vm_ids: "aws_sdk_evs.types.vm_id_list.VmIdList",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.create_entitlement_response.CreateEntitlementResponse":
        """<p>Creates a Windows Server License entitlement for virtual machines in an Amazon EVS environment using the provided vCenter Server connector. This is an asynchronous operation. Amazon EVS validates the specified virtual machines before starting usage tracking.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the entitlement creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment to create the entitlement in.</p>
            connector_id: <p>A unique ID for the connector associated with the entitlement.</p>
            entitlement_type: <p>The type of entitlement to create.</p>
            vm_ids: <p>The list of VMware vSphere virtual machine managed object IDs to create entitlements for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.create_entitlement_request.CreateEntitlementRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.create_entitlement_response.CreateEntitlementResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_entitlement

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_entitlement.create_entitlement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.create_entitlement_request.CreateEntitlementRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["connector_id"] = connector_id
        input["entitlement_type"] = entitlement_type
        input["vm_ids"] = vm_ids

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_environment_connector(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        type: "aws_sdk_evs.types.connector_type.ConnectorType",
        appliance_fqdn: "aws_sdk_evs.types.appliance_fqdn.ApplianceFqdn",
        secret_identifier: "aws_sdk_evs.types.secret_identifier.SecretIdentifier",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.create_environment_connector_response.CreateEnvironmentConnectorResponse":
        """<p>Creates a connector for an Amazon EVS environment. A connector establishes a connection to a VCF appliance, such as vCenter, using a fully qualified domain name and an Amazon Web Services Secrets Manager secret that stores the appliance credentials.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the connector creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment to create the connector in.</p>
            type: <p>The type of connector to create.</p>
            appliance_fqdn: <p>The fully qualified domain name (FQDN) of the VCF appliance that the connector targets.</p>
            secret_identifier: <p>The ARN or name of the Amazon Web Services Secrets Manager secret that stores the credentials for the VCF appliance.</p> <important> <p>Do not use credentials with Administrator privileges. We recommend using a service account with the minimum required permissions.</p> </important>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.create_environment_connector_request.CreateEnvironmentConnectorRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.create_environment_connector_response.CreateEnvironmentConnectorResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_environment_connector

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_environment_connector.create_environment_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.create_environment_connector_request.CreateEnvironmentConnectorRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["type"] = type
        input["appliance_fqdn"] = appliance_fqdn
        input["secret_identifier"] = secret_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_environment_host(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        host: "aws_sdk_evs.types.host_info_for_create.HostInfoForCreate",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
        esx_version: Optional["aws_sdk_evs.types.esx_version.EsxVersion"] = None,
    ) -> "aws_sdk_evs.types.create_environment_host_response.CreateEnvironmentHostResponse":
        """<p>Creates an ESX host and adds it to an Amazon EVS environment. Amazon EVS supports 4-32 hosts per environment.</p> <p>This action can only be used after the Amazon EVS environment is deployed.</p> <p>You can use the <code>dedicatedHostId</code> parameter to specify an Amazon EC2 Dedicated Host for ESX host creation.</p> <p> You can use the <code>placementGroupId</code> parameter to specify a cluster or partition placement group to launch EC2 instances into.</p> <note> <p>If you don't specify an ESX version when adding hosts using <code>CreateEnvironmentHost</code> action, Amazon EVS automatically uses the default ESX version associated with your environment's VCF version. To find the default ESX version for a particular VCF version, use the <code>GetVersions</code> action.</p> </note> <note> <p>You cannot use the <code>dedicatedHostId</code> and <code>placementGroupId</code> parameters together in the same <code>CreateEnvironmentHost</code> action. This results in a <code>ValidationException</code> response.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the host creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment that the host is added to.</p>
            host: <p>The host that is created and added to the environment.</p>
            esx_version: <p>The ESX version to use for the host.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.create_environment_host_request.CreateEnvironmentHostRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.create_environment_host_response.CreateEnvironmentHostResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_environment_host

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_environment_host.create_environment_host(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.create_environment_host_request.CreateEnvironmentHostRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["host"] = host
        if esx_version is not None:
            input["esx_version"] = esx_version

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_entitlement(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        connector_id: "aws_sdk_evs.types.connector_id.ConnectorId",
        entitlement_type: "aws_sdk_evs.types.entitlement_type.EntitlementType",
        vm_ids: "aws_sdk_evs.types.vm_id_list.VmIdList",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.delete_entitlement_response.DeleteEntitlementResponse":
        """<p>Deletes a Windows Server License entitlement for virtual machines in an Amazon EVS environment. Deleting an entitlement stops usage tracking for the specified virtual machines.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the entitlement deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment that the entitlement belongs to.</p>
            connector_id: <p>A unique ID for the connector associated with the entitlement.</p>
            entitlement_type: <p>The type of entitlement to delete.</p>
            vm_ids: <p>The list of VMware vSphere virtual machine managed object IDs to delete entitlements for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.delete_entitlement_request.DeleteEntitlementRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.delete_entitlement_response.DeleteEntitlementResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_entitlement

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_entitlement.delete_entitlement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.delete_entitlement_request.DeleteEntitlementRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["connector_id"] = connector_id
        input["entitlement_type"] = entitlement_type
        input["vm_ids"] = vm_ids

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_environment_connector(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        connector_id: "aws_sdk_evs.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.delete_environment_connector_response.DeleteEnvironmentConnectorResponse":
        """<p>Deletes a connector from an Amazon EVS environment.</p> <note> <p>Before deleting a connector, you must remove all entitlements that are associated with the same vCenter.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the connector deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment that the connector belongs to.</p>
            connector_id: <p>A unique ID for the connector to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.delete_environment_connector_request.DeleteEnvironmentConnectorRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.delete_environment_connector_response.DeleteEnvironmentConnectorResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_environment_connector

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_environment_connector.delete_environment_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.delete_environment_connector_request.DeleteEnvironmentConnectorRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["connector_id"] = connector_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_environment_host(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        host_name: "aws_sdk_evs.types.host_name.HostName",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.delete_environment_host_response.DeleteEnvironmentHostResponse":
        """<p>Deletes a host from an Amazon EVS environment.</p> <note> <p>Before deleting a host, you must unassign and decommission the host from within the SDDC Manager user interface. Not doing so could impact the availability of your virtual machines or result in data loss.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the host deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the host's environment.</p>
            host_name: <p>The DNS hostname associated with the host to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.delete_environment_host_request.DeleteEnvironmentHostRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.delete_environment_host_response.DeleteEnvironmentHostResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_environment_host

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_environment_host.delete_environment_host(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.delete_environment_host_request.DeleteEnvironmentHostRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["host_name"] = host_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_eip_from_vlan(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        vlan_name: str,
        association_id: "aws_sdk_evs.types.association_id.AssociationId",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.disassociate_eip_from_vlan_response.DisassociateEipFromVlanResponse":
        """<p>Disassociates an Elastic IP address from a public HCX VLAN. This operation is only allowed for public HCX VLANs at this time.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment containing the VLAN that the Elastic IP address disassociates from.</p>
            vlan_name: <p>The name of the VLAN. <code>hcx</code> is the only accepted VLAN name at this time.</p>
            association_id: <p> A unique ID for the Elastic IP address association.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.disassociate_eip_from_vlan_request.DisassociateEipFromVlanRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.disassociate_eip_from_vlan_response.DisassociateEipFromVlanResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.disassociate_eip_from_vlan

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.disassociate_eip_from_vlan.disassociate_eip_from_vlan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.disassociate_eip_from_vlan_request.DisassociateEipFromVlanRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["vlan_name"] = vlan_name
        input["association_id"] = association_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_depot_url(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        rotate: Optional[bool] = None,
    ) -> "aws_sdk_evs.types.get_depot_url_response.GetDepotUrlResponse":
        """<p>Returns a URL and authentication token for accessing the Amazon EVS Custom Addon depot. Configure the depot URL as a download source in vSphere Lifecycle Manager (vLCM) to sync and install the Amazon EVS Custom Addon.</p> <p>The depot URL remains active until you rotate the authentication token by calling this action with <code>rotate</code> set to <code>true</code>.</p>

        Args:
            environment_id: <p>The unique ID of the Amazon EVS environment to get the depot URL for.</p>
            rotate: <p>Revokes the current authentication token and returns a new depot URL with a new token. Previously issued depot URLs will stop working within 5 minutes of rotation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.get_depot_url_request.GetDepotUrlRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.get_depot_url_response.GetDepotUrlResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.get_depot_url

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.get_depot_url.get_depot_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.get_depot_url_request.GetDepotUrlRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        if rotate is not None:
            input["rotate"] = rotate

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_environment_connectors(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_evs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_evs.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_evs.types.list_environment_connectors_response.ListEnvironmentConnectorsResponse":
        """<p>Lists the connectors within an environment. Returns the status of each connector and its applicable checks, among other connector details.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            environment_id: <p>A unique ID for the environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.list_environment_connectors_request.ListEnvironmentConnectorsRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.list_environment_connectors_response.ListEnvironmentConnectorsResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environment_connectors

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environment_connectors.list_environment_connectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.list_environment_connectors_request.ListEnvironmentConnectorsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["environment_id"] = environment_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_environment_hosts(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_evs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_evs.types.max_results.MaxResults"] = None,
    ) -> (
        "aws_sdk_evs.types.list_environment_hosts_response.ListEnvironmentHostsResponse"
    ):
        """<p>List the hosts within an environment.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            environment_id: <p>A unique ID for the environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.list_environment_hosts_request.ListEnvironmentHostsRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.list_environment_hosts_response.ListEnvironmentHostsResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environment_hosts

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environment_hosts.list_environment_hosts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.list_environment_hosts_request.ListEnvironmentHostsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["environment_id"] = environment_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_environment_vlans(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_evs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_evs.types.max_results.MaxResults"] = None,
    ) -> (
        "aws_sdk_evs.types.list_environment_vlans_response.ListEnvironmentVlansResponse"
    ):
        """<p>Lists environment VLANs that are associated with the specified environment.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            environment_id: <p>A unique ID for the environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.list_environment_vlans_request.ListEnvironmentVlansRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.list_environment_vlans_response.ListEnvironmentVlansResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environment_vlans

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environment_vlans.list_environment_vlans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.list_environment_vlans_request.ListEnvironmentVlansRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["environment_id"] = environment_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_vm_entitlements(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        connector_id: "aws_sdk_evs.types.connector_id.ConnectorId",
        entitlement_type: "aws_sdk_evs.types.entitlement_type.EntitlementType",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_evs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_evs.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_evs.types.list_vm_entitlements_response.ListVmEntitlementsResponse":
        """<p>Lists the Windows Server License entitlements for virtual machines in an Amazon EVS environment. Returns existing entitlements for virtual machines associated with the specified environment and connector.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            environment_id: <p>A unique ID for the environment.</p>
            connector_id: <p>A unique ID for the connector.</p>
            entitlement_type: <p>The type of entitlement to list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.list_vm_entitlements_request.ListVmEntitlementsRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.list_vm_entitlements_response.ListVmEntitlementsResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_vm_entitlements

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_vm_entitlements.list_vm_entitlements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.list_vm_entitlements_request.ListVmEntitlementsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["environment_id"] = environment_id
        input["connector_id"] = connector_id
        input["entitlement_type"] = entitlement_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_environment_connector(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        connector_id: "aws_sdk_evs.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[evsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
        appliance_fqdn: Optional[
            "aws_sdk_evs.types.appliance_fqdn.ApplianceFqdn"
        ] = None,
        secret_identifier: Optional[
            "aws_sdk_evs.types.secret_identifier.SecretIdentifier"
        ] = None,
    ) -> "aws_sdk_evs.types.update_environment_connector_response.UpdateEnvironmentConnectorResponse":
        """<p>Updates a connector for an Amazon EVS environment. You can update the Amazon Web Services Secrets Manager secret ARN or the appliance FQDN to reconfigure the connector metadata.</p> <note> <p>You cannot update both the secret and the FQDN in the same request.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the connector update request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment that the connector belongs to.</p>
            connector_id: <p>A unique ID for the connector to update.</p>
            appliance_fqdn: <p>The new fully qualified domain name (FQDN) of the VCF appliance that the connector connects to.</p>
            secret_identifier: <p>The new ARN or name of the Amazon Web Services Secrets Manager secret that stores the credentials for the VCF appliance.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.update_environment_connector_request.UpdateEnvironmentConnectorRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.update_environment_connector_response.UpdateEnvironmentConnectorResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.update_environment_connector

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.update_environment_connector.update_environment_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.update_environment_connector_request.UpdateEnvironmentConnectorRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["connector_id"] = connector_id
        if appliance_fqdn is not None:
            input["appliance_fqdn"] = appliance_fqdn
        if secret_identifier is not None:
            input["secret_identifier"] = secret_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncEnvironmentResource:
    def __init__(self, service: AsyncevsClient) -> None:
        self._service = service

    async def create(
        self,
        vpc_id: "aws_sdk_evs.types.vpc_id.VpcId",
        service_access_subnet_id: "aws_sdk_evs.types.subnet_id.SubnetId",
        vcf_version: "aws_sdk_evs.types.vcf_version.VcfVersion",
        terms_accepted: bool,
        license_info: "aws_sdk_evs.types.license_info_list.LicenseInfoList",
        initial_vlans: "aws_sdk_evs.types.initial_vlans.InitialVlans",
        hosts: "aws_sdk_evs.types.host_info_for_create_list.HostInfoForCreateList",
        connectivity_info: "aws_sdk_evs.types.connectivity_info.ConnectivityInfo",
        vcf_hostnames: "aws_sdk_evs.types.vcf_hostnames.VcfHostnames",
        site_id: str,
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
        environment_name: Optional[
            "aws_sdk_evs.types.environment_name.EnvironmentName"
        ] = None,
        kms_key_id: Optional[str] = None,
        tags: Optional["aws_sdk_evs.types.request_tag_map.RequestTagMap"] = None,
        service_access_security_groups: Optional[
            "aws_sdk_evs.types.service_access_security_groups.ServiceAccessSecurityGroups"
        ] = None,
    ) -> "aws_sdk_evs.types.create_environment_response.CreateEnvironmentResponse":
        """<p>Creates an Amazon EVS environment that runs VCF software, such as SDDC Manager, NSX Manager, and vCenter Server.</p> <p>During environment creation, Amazon EVS performs validations on DNS settings, provisions VLAN subnets and hosts, and deploys the supplied version of VCF.</p> <p>It can take several hours to create an environment. After the deployment completes, you can configure VCF in the vSphere user interface according to your needs.</p> <important> <p>When creating a new environment, the default ESX version for the selected VCF version will be used, you cannot choose a specific ESX version in <code>CreateEnvironment</code> action. When a host has been added with a specific ESX version, it can only be upgraded using vCenter Lifecycle Manager.</p> </important> <note> <p>You cannot use the <code>dedicatedHostId</code> and <code>placementGroupId</code> parameters together in the same <code>CreateEnvironment</code> action. This results in a <code>ValidationException</code> response.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_name: <p>The name to give to your environment. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphanumeric character, and can't be longer than 100 characters. The name must be unique within the Amazon Web Services Region and Amazon Web Services account that you're creating the environment in.</p>
            kms_key_id: <p>A unique ID for the customer-managed KMS key that is used to encrypt the VCF credential pairs for SDDC Manager, NSX Manager, and vCenter appliances. These credentials are stored in Amazon Web Services Secrets Manager.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>
            service_access_security_groups: <p>The security group that controls communication between the Amazon EVS control plane and VPC. The default security group is used if a custom security group isn't specified.</p> <p>The security group should allow access to the following.</p> <ul> <li> <p>TCP/UDP access to the DNS servers</p> </li> <li> <p>HTTPS/SSH access to the host management VLAN subnet</p> </li> <li> <p>HTTPS/SSH access to the Management VM VLAN subnet</p> </li> </ul> <p>You should avoid modifying the security group rules after deployment, as this can break the persistent connection between the Amazon EVS control plane and VPC. This can cause future environment actions like adding or removing hosts to fail.</p>
            vpc_id: <p>A unique ID for the VPC that the environment is deployed inside.</p> <p>Amazon EVS requires that all VPC subnets exist in a single Availability Zone in a Region where the service is available.</p> <p>The VPC that you specify must have a valid DHCP option set with domain name, at least two DNS servers, and an NTP server. These settings are used to configure your VCF appliances and hosts. The VPC cannot be used with any other deployed Amazon EVS environment. Amazon EVS does not provide multi-VPC support for environments at this time.</p> <p>Amazon EVS does not support the following Amazon Web Services networking options for NSX overlay connectivity: cross-Region VPC peering, Amazon S3 gateway endpoints, or Amazon Web Services Direct Connect virtual private gateway associations.</p> <note> <p>Ensure that you specify a VPC that is adequately sized to accommodate the Amazon EVS subnets.</p> </note>
            service_access_subnet_id: <p>The subnet that is used to establish connectivity between the Amazon EVS control plane and VPC. Amazon EVS uses this subnet to validate mandatory DNS records for your VCF appliances and hosts and create the environment.</p>
            vcf_version: <p> The VCF version to use for the environment.</p>
            terms_accepted: <p>Customer confirmation that the customer has purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment. Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance. Amazon EVS does not validate license keys. To validate license keys, visit the Broadcom support portal.</p>
            license_info: <p>The license information that Amazon EVS requires to create an environment. Amazon EVS requires two license keys: a VCF solution key and a vSAN license key. The VCF solution key must meet minimum core requirements, and the vSAN license key must meet minimum capacity requirements for your selected instance type.</p> <p>For information about minimum license requirements, see <a href=\"https://docs.aws.amazon.com/evs/latest/userguide/vcf-license-mgmt.html\">the VCF subscriptions section</a> in the <i>Amazon EVS User Guide</i>.</p> <p>VCF licenses can be used for only one Amazon EVS environment. Amazon EVS does not support reuse of VCF licenses for multiple environments.</p> <p>VCF license information can be retrieved from the Broadcom portal.</p>
            initial_vlans: <p>The initial VLAN subnets for the Amazon EVS environment.</p> <note> <p>For each Amazon EVS VLAN subnet, you must specify a non-overlapping CIDR block. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24.</p> </note>
            hosts: <p>The ESX hosts to add to the environment. Amazon EVS requires that you provide details for a minimum of 4 hosts during environment creation.</p> <p>For each host, you must provide the desired hostname, EC2 SSH keypair name, and EC2 instance type. Optionally, you can also provide a partition or cluster placement group to use, or use Amazon EC2 Dedicated Hosts.</p>
            connectivity_info: <p> The connectivity configuration for the environment. Amazon EVS requires that you specify two route server peer IDs. During environment creation, the route server endpoints peer with the NSX edges over the NSX uplink subnet, providing BGP-based dynamic routing for overlay networks.</p>
            vcf_hostnames: <p>The DNS hostnames for the virtual machines that host the VCF management appliances. Amazon EVS requires that you provide DNS hostnames for the following appliances: vCenter, NSX Manager, SDDC Manager, and Cloud Builder.</p>
            site_id: <p>The Broadcom Site ID that is allocated to you as part of your electronic software delivery. This ID allows customer access to the Broadcom portal, and is provided to you by Broadcom at the close of your software contract or contract renewal. Amazon EVS uses the Broadcom Site ID that you provide to meet Broadcom VCF license usage reporting requirements for Amazon EVS.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.create_environment_request.CreateEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.create_environment_response.CreateEnvironmentResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_environment

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_environment.async_create_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.create_environment_request.CreateEnvironmentRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        if environment_name is not None:
            input["environment_name"] = environment_name
        if kms_key_id is not None:
            input["kms_key_id"] = kms_key_id
        if tags is not None:
            input["tags"] = tags
        if service_access_security_groups is not None:
            input["service_access_security_groups"] = service_access_security_groups
        input["vpc_id"] = vpc_id
        input["service_access_subnet_id"] = service_access_subnet_id
        input["vcf_version"] = vcf_version
        input["terms_accepted"] = terms_accepted
        input["license_info"] = license_info
        input["initial_vlans"] = initial_vlans
        input["hosts"] = hosts
        input["connectivity_info"] = connectivity_info
        input["vcf_hostnames"] = vcf_hostnames
        input["site_id"] = site_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
    ) -> "aws_sdk_evs.types.get_environment_response.GetEnvironmentResponse":
        """<p>Returns a description of the specified environment.</p>

        Args:
            environment_id: <p>A unique ID for the environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.get_environment_request.GetEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.get_environment_response.GetEnvironmentResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.get_environment

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.get_environment.async_get_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.get_environment_request.GetEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.delete_environment_response.DeleteEnvironmentResponse":
        """<p>Deletes an Amazon EVS environment.</p> <p>Amazon EVS environments will only be enabled for deletion once the hosts are deleted. You can delete hosts using the <code>DeleteEnvironmentHost</code> action.</p> <p>Environment deletion also deletes the associated Amazon EVS VLAN subnets and Amazon Web Services Secrets Manager secrets that Amazon EVS created. Amazon Web Services resources that you create are not deleted. These resources may continue to incur costs.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID associated with the environment to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.delete_environment_request.DeleteEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.delete_environment_response.DeleteEnvironmentResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_environment

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_environment.async_delete_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.delete_environment_request.DeleteEnvironmentRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_evs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_evs.types.max_results.MaxResults"] = None,
        state: Optional[
            "aws_sdk_evs.types.environment_state_list.EnvironmentStateList"
        ] = None,
    ) -> "aws_sdk_evs.types.list_environments_response.ListEnvironmentsResponse":
        """<p>Lists the Amazon EVS environments in your Amazon Web Services account in the specified Amazon Web Services Region.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            state: <p>The state of an environment. Used to filter response results to return only environments with the specified <code>environmentState</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.list_environments_response.ListEnvironmentsResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environments

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environments.async_list_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.list_environments_request.ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if state is not None:
            input["state"] = state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_eip_to_vlan(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        vlan_name: str,
        allocation_id: "aws_sdk_evs.types.allocation_id.AllocationId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.associate_eip_to_vlan_response.AssociateEipToVlanResponse":
        """<p>Associates an Elastic IP address with a public HCX VLAN. This operation is only allowed for public HCX VLANs at this time.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment containing the VLAN that the Elastic IP address associates with.</p>
            vlan_name: <p>The name of the VLAN. <code>hcx</code> is the only accepted VLAN name at this time.</p>
            allocation_id: <p>The Elastic IP address allocation ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.associate_eip_to_vlan_request.AssociateEipToVlanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.associate_eip_to_vlan_response.AssociateEipToVlanResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.associate_eip_to_vlan

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.associate_eip_to_vlan.async_associate_eip_to_vlan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.associate_eip_to_vlan_request.AssociateEipToVlanRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["vlan_name"] = vlan_name
        input["allocation_id"] = allocation_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_entitlement(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        connector_id: "aws_sdk_evs.types.connector_id.ConnectorId",
        entitlement_type: "aws_sdk_evs.types.entitlement_type.EntitlementType",
        vm_ids: "aws_sdk_evs.types.vm_id_list.VmIdList",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.create_entitlement_response.CreateEntitlementResponse":
        """<p>Creates a Windows Server License entitlement for virtual machines in an Amazon EVS environment using the provided vCenter Server connector. This is an asynchronous operation. Amazon EVS validates the specified virtual machines before starting usage tracking.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the entitlement creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment to create the entitlement in.</p>
            connector_id: <p>A unique ID for the connector associated with the entitlement.</p>
            entitlement_type: <p>The type of entitlement to create.</p>
            vm_ids: <p>The list of VMware vSphere virtual machine managed object IDs to create entitlements for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.create_entitlement_request.CreateEntitlementRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.create_entitlement_response.CreateEntitlementResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_entitlement

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_entitlement.async_create_entitlement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.create_entitlement_request.CreateEntitlementRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["connector_id"] = connector_id
        input["entitlement_type"] = entitlement_type
        input["vm_ids"] = vm_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_environment_connector(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        type: "aws_sdk_evs.types.connector_type.ConnectorType",
        appliance_fqdn: "aws_sdk_evs.types.appliance_fqdn.ApplianceFqdn",
        secret_identifier: "aws_sdk_evs.types.secret_identifier.SecretIdentifier",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.create_environment_connector_response.CreateEnvironmentConnectorResponse":
        """<p>Creates a connector for an Amazon EVS environment. A connector establishes a connection to a VCF appliance, such as vCenter, using a fully qualified domain name and an Amazon Web Services Secrets Manager secret that stores the appliance credentials.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the connector creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment to create the connector in.</p>
            type: <p>The type of connector to create.</p>
            appliance_fqdn: <p>The fully qualified domain name (FQDN) of the VCF appliance that the connector targets.</p>
            secret_identifier: <p>The ARN or name of the Amazon Web Services Secrets Manager secret that stores the credentials for the VCF appliance.</p> <important> <p>Do not use credentials with Administrator privileges. We recommend using a service account with the minimum required permissions.</p> </important>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.create_environment_connector_request.CreateEnvironmentConnectorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.create_environment_connector_response.CreateEnvironmentConnectorResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_environment_connector

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_environment_connector.async_create_environment_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.create_environment_connector_request.CreateEnvironmentConnectorRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["type"] = type
        input["appliance_fqdn"] = appliance_fqdn
        input["secret_identifier"] = secret_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_environment_host(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        host: "aws_sdk_evs.types.host_info_for_create.HostInfoForCreate",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
        esx_version: Optional["aws_sdk_evs.types.esx_version.EsxVersion"] = None,
    ) -> "aws_sdk_evs.types.create_environment_host_response.CreateEnvironmentHostResponse":
        """<p>Creates an ESX host and adds it to an Amazon EVS environment. Amazon EVS supports 4-32 hosts per environment.</p> <p>This action can only be used after the Amazon EVS environment is deployed.</p> <p>You can use the <code>dedicatedHostId</code> parameter to specify an Amazon EC2 Dedicated Host for ESX host creation.</p> <p> You can use the <code>placementGroupId</code> parameter to specify a cluster or partition placement group to launch EC2 instances into.</p> <note> <p>If you don't specify an ESX version when adding hosts using <code>CreateEnvironmentHost</code> action, Amazon EVS automatically uses the default ESX version associated with your environment's VCF version. To find the default ESX version for a particular VCF version, use the <code>GetVersions</code> action.</p> </note> <note> <p>You cannot use the <code>dedicatedHostId</code> and <code>placementGroupId</code> parameters together in the same <code>CreateEnvironmentHost</code> action. This results in a <code>ValidationException</code> response.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the host creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment that the host is added to.</p>
            host: <p>The host that is created and added to the environment.</p>
            esx_version: <p>The ESX version to use for the host.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.create_environment_host_request.CreateEnvironmentHostRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.create_environment_host_response.CreateEnvironmentHostResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_environment_host

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.create_environment_host.async_create_environment_host(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.create_environment_host_request.CreateEnvironmentHostRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["host"] = host
        if esx_version is not None:
            input["esx_version"] = esx_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_entitlement(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        connector_id: "aws_sdk_evs.types.connector_id.ConnectorId",
        entitlement_type: "aws_sdk_evs.types.entitlement_type.EntitlementType",
        vm_ids: "aws_sdk_evs.types.vm_id_list.VmIdList",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.delete_entitlement_response.DeleteEntitlementResponse":
        """<p>Deletes a Windows Server License entitlement for virtual machines in an Amazon EVS environment. Deleting an entitlement stops usage tracking for the specified virtual machines.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the entitlement deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment that the entitlement belongs to.</p>
            connector_id: <p>A unique ID for the connector associated with the entitlement.</p>
            entitlement_type: <p>The type of entitlement to delete.</p>
            vm_ids: <p>The list of VMware vSphere virtual machine managed object IDs to delete entitlements for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.delete_entitlement_request.DeleteEntitlementRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.delete_entitlement_response.DeleteEntitlementResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_entitlement

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_entitlement.async_delete_entitlement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.delete_entitlement_request.DeleteEntitlementRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["connector_id"] = connector_id
        input["entitlement_type"] = entitlement_type
        input["vm_ids"] = vm_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_environment_connector(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        connector_id: "aws_sdk_evs.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.delete_environment_connector_response.DeleteEnvironmentConnectorResponse":
        """<p>Deletes a connector from an Amazon EVS environment.</p> <note> <p>Before deleting a connector, you must remove all entitlements that are associated with the same vCenter.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the connector deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment that the connector belongs to.</p>
            connector_id: <p>A unique ID for the connector to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.delete_environment_connector_request.DeleteEnvironmentConnectorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.delete_environment_connector_response.DeleteEnvironmentConnectorResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_environment_connector

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_environment_connector.async_delete_environment_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.delete_environment_connector_request.DeleteEnvironmentConnectorRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["connector_id"] = connector_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_environment_host(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        host_name: "aws_sdk_evs.types.host_name.HostName",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.delete_environment_host_response.DeleteEnvironmentHostResponse":
        """<p>Deletes a host from an Amazon EVS environment.</p> <note> <p>Before deleting a host, you must unassign and decommission the host from within the SDDC Manager user interface. Not doing so could impact the availability of your virtual machines or result in data loss.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the host deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the host's environment.</p>
            host_name: <p>The DNS hostname associated with the host to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.delete_environment_host_request.DeleteEnvironmentHostRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.delete_environment_host_response.DeleteEnvironmentHostResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_environment_host

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.delete_environment_host.async_delete_environment_host(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.delete_environment_host_request.DeleteEnvironmentHostRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["host_name"] = host_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_eip_from_vlan(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        vlan_name: str,
        association_id: "aws_sdk_evs.types.association_id.AssociationId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_evs.types.disassociate_eip_from_vlan_response.DisassociateEipFromVlanResponse":
        """<p>Disassociates an Elastic IP address from a public HCX VLAN. This operation is only allowed for public HCX VLANs at this time.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment containing the VLAN that the Elastic IP address disassociates from.</p>
            vlan_name: <p>The name of the VLAN. <code>hcx</code> is the only accepted VLAN name at this time.</p>
            association_id: <p> A unique ID for the Elastic IP address association.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.disassociate_eip_from_vlan_request.DisassociateEipFromVlanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.disassociate_eip_from_vlan_response.DisassociateEipFromVlanResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.disassociate_eip_from_vlan

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.disassociate_eip_from_vlan.async_disassociate_eip_from_vlan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.disassociate_eip_from_vlan_request.DisassociateEipFromVlanRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["vlan_name"] = vlan_name
        input["association_id"] = association_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_depot_url(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        rotate: Optional[bool] = None,
    ) -> "aws_sdk_evs.types.get_depot_url_response.GetDepotUrlResponse":
        """<p>Returns a URL and authentication token for accessing the Amazon EVS Custom Addon depot. Configure the depot URL as a download source in vSphere Lifecycle Manager (vLCM) to sync and install the Amazon EVS Custom Addon.</p> <p>The depot URL remains active until you rotate the authentication token by calling this action with <code>rotate</code> set to <code>true</code>.</p>

        Args:
            environment_id: <p>The unique ID of the Amazon EVS environment to get the depot URL for.</p>
            rotate: <p>Revokes the current authentication token and returns a new depot URL with a new token. Previously issued depot URLs will stop working within 5 minutes of rotation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.get_depot_url_request.GetDepotUrlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.get_depot_url_response.GetDepotUrlResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.get_depot_url

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.get_depot_url.async_get_depot_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.get_depot_url_request.GetDepotUrlRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        if rotate is not None:
            input["rotate"] = rotate

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_environment_connectors(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_evs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_evs.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_evs.types.list_environment_connectors_response.ListEnvironmentConnectorsResponse":
        """<p>Lists the connectors within an environment. Returns the status of each connector and its applicable checks, among other connector details.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            environment_id: <p>A unique ID for the environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.list_environment_connectors_request.ListEnvironmentConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.list_environment_connectors_response.ListEnvironmentConnectorsResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environment_connectors

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environment_connectors.async_list_environment_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.list_environment_connectors_request.ListEnvironmentConnectorsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["environment_id"] = environment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_environment_hosts(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_evs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_evs.types.max_results.MaxResults"] = None,
    ) -> (
        "aws_sdk_evs.types.list_environment_hosts_response.ListEnvironmentHostsResponse"
    ):
        """<p>List the hosts within an environment.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            environment_id: <p>A unique ID for the environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.list_environment_hosts_request.ListEnvironmentHostsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.list_environment_hosts_response.ListEnvironmentHostsResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environment_hosts

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environment_hosts.async_list_environment_hosts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.list_environment_hosts_request.ListEnvironmentHostsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["environment_id"] = environment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_environment_vlans(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_evs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_evs.types.max_results.MaxResults"] = None,
    ) -> (
        "aws_sdk_evs.types.list_environment_vlans_response.ListEnvironmentVlansResponse"
    ):
        """<p>Lists environment VLANs that are associated with the specified environment.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            environment_id: <p>A unique ID for the environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.list_environment_vlans_request.ListEnvironmentVlansRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.list_environment_vlans_response.ListEnvironmentVlansResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environment_vlans

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_environment_vlans.async_list_environment_vlans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.list_environment_vlans_request.ListEnvironmentVlansRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["environment_id"] = environment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_vm_entitlements(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        connector_id: "aws_sdk_evs.types.connector_id.ConnectorId",
        entitlement_type: "aws_sdk_evs.types.entitlement_type.EntitlementType",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_evs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_evs.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_evs.types.list_vm_entitlements_response.ListVmEntitlementsResponse":
        """<p>Lists the Windows Server License entitlements for virtual machines in an Amazon EVS environment. Returns existing entitlements for virtual machines associated with the specified environment and connector.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            environment_id: <p>A unique ID for the environment.</p>
            connector_id: <p>A unique ID for the connector.</p>
            entitlement_type: <p>The type of entitlement to list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.list_vm_entitlements_request.ListVmEntitlementsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.list_vm_entitlements_response.ListVmEntitlementsResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_vm_entitlements

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_vm_entitlements.async_list_vm_entitlements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.list_vm_entitlements_request.ListVmEntitlementsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["environment_id"] = environment_id
        input["connector_id"] = connector_id
        input["entitlement_type"] = entitlement_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_environment_connector(
        self,
        environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId",
        connector_id: "aws_sdk_evs.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["aws_sdk_evs.types.client_token.ClientToken"] = None,
        appliance_fqdn: Optional[
            "aws_sdk_evs.types.appliance_fqdn.ApplianceFqdn"
        ] = None,
        secret_identifier: Optional[
            "aws_sdk_evs.types.secret_identifier.SecretIdentifier"
        ] = None,
    ) -> "aws_sdk_evs.types.update_environment_connector_response.UpdateEnvironmentConnectorResponse":
        """<p>Updates a connector for an Amazon EVS environment. You can update the Amazon Web Services Secrets Manager secret ARN or the appliance FQDN to reconfigure the connector metadata.</p> <note> <p>You cannot update both the secret and the FQDN in the same request.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the connector update request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment that the connector belongs to.</p>
            connector_id: <p>A unique ID for the connector to update.</p>
            appliance_fqdn: <p>The new fully qualified domain name (FQDN) of the VCF appliance that the connector connects to.</p>
            secret_identifier: <p>The new ARN or name of the Amazon Web Services Secrets Manager secret that stores the credentials for the VCF appliance.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.update_environment_connector_request.UpdateEnvironmentConnectorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.update_environment_connector_response.UpdateEnvironmentConnectorResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.update_environment_connector

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.update_environment_connector.async_update_environment_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_evs.types.update_environment_connector_request.UpdateEnvironmentConnectorRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["connector_id"] = connector_id
        if appliance_fqdn is not None:
            input["appliance_fqdn"] = appliance_fqdn
        if secret_identifier is not None:
            input["secret_identifier"] = secret_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
